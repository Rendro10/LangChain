from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence


load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a tweet on {topic} for tweeter post',
    input_variable = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a post on {topic} for linkedIn post',
    input_variable = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedIn': RunnableSequence(prompt2, model, parser)
})

res = chain.invoke({'topic': 'AI in the workplace'})

print(res)