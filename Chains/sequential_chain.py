from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Eg: we need to build an application where I will give the topic like cricker and it will generate a detailed
# report on it and then we will again send that report to the same model to extract 5 majore points out of it.


load_dotenv()

prompt1 = PromptTemplate(
    template='You are a helpful assistant that generate a detailed report on {topic}',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='You are a helpful assistant that generate five pointer summary from the following report: {report}',
    input_variables=['report'],
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'cricket'})

# print(result)

chain.get_graph().print_ascii()
