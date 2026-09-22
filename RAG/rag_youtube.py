"""
RAG over a YouTube transcript using LangChain + OpenAI + FAISS.
Converted from Colab notebook to run locally in VS Code.
"""
from dotenv import load_dotenv


from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
# ---------------- Step 1a - Indexing (Document Ingestion) ----------------
video_id = "Gfr50f6ZBvo"  # only the ID, not full URL

try:
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=["en"])
    transcript_list = transcript.to_raw_data()
    text = " ".join(x["text"] for x in transcript_list)
    print(text[:500], "...\n")  # preview only
except Exception as e:
    raise SystemExit(f"Could not fetch transcript: {e}")


# ---------------- Step 1b - Indexing (Text Splitting) ----------------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([text])
print("Number of chunks:", len(chunks))
if len(chunks) > 100:
    print("Chunk 100:", chunks[100], "\n")


# ------- Step 1c & 1d - Embedding Generation and Vector Store -------
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = FAISS.from_documents(chunks, embeddings)

print("Sample index -> docstore ids:", list(vector_store.index_to_docstore_id.items())[:3])
first_id = next(iter(vector_store.index_to_docstore_id.values()))
print("First stored doc:", vector_store.get_by_ids([first_id]), "\n")


# ---------------- Step 2 - Retrieval ----------------
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
print("Retrieval test ('What is deepmind'):")
print(retriever.invoke("What is deepmind"), "\n")


# ---------------- Step 3 - Augmentation ----------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables=["context", "question"],
)

question = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
final_prompt = prompt.invoke({"context": context_text, "question": question})
print("Final prompt:\n", final_prompt, "\n")


# ---------------- Step 4 - Generation ----------------
answer = llm.invoke(final_prompt)
print("Answer:\n", answer.content, "\n")


# ---------------- Building a Chain ----------------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough(),
})

print("Parallel chain test ('who is Demis'):")
print(parallel_chain.invoke("who is Demis"), "\n")

parser = StrOutputParser()
main_chain = parallel_chain | prompt | llm | parser

print("Summary:\n", main_chain.invoke("Can you summarize the video"))
