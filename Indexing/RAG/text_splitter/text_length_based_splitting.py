from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\\Users\\114-user\\OneDrive\\Desktop\\LangChain\\RAG\\document_loader\\dl-curriculum.pdf")
docs = loader.load()


text_splitter = CharacterTextSplitter(
    separator='',
    chunk_size=100,
    chunk_overlap=20
)

res = text_splitter.split_documents(docs)

print(res[0].page_content)
# print(res[0].metadata)