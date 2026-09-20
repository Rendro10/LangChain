from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()



url = "https://www.amazon.in"
loader = WebBaseLoader(url)
docs = loader.load()


model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="write the answer of the following question: {question} from the following text {text}",
    input_variables=["question", "text"]
)

chain = prompt | model | parser

res = chain.invoke({"question": "What is the website about?", "text": docs[0].page_content})

print(res)



  