from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='You are a helpful assistant that generate five interesting facts about {topic}',
    input_variables=['topic']
)


model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

final_result = chain.invoke({'topic':'Python programming language'})

print(final_result)

