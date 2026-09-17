from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence


load_dotenv()

prompt1 = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variable = ['topic']
)

prompt2 = PromptTemplate(
    template = 'please explain the joke about {text}',
    input_variable = ['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

res = chain.invoke({'topic': 'Human'})

print(res)
