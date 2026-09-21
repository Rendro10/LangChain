from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = TextLoader('C:\\Users\\114-user\\OneDrive\\Desktop\\LangChain\\RAG\\document_loader\\cricket.text', encoding='utf-8')

docs = loader.load()


load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'write a summary of the following poem: {poem}',
    input_variables = ['poem'],
)

chain = prompt | model | parser

res = chain.invoke({'poem': docs[0].page_content})

print(res)







# print(type(docs))
# print(len(docs))

# print(docs[0].page_content)
# print(docs[0].metadata)