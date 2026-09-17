from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()



promt1 = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variable = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'please explain the joke about {text}',
    input_variable = ['text']
)

joke_generation_chain = RunnableSequence(promt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generation_chain, parallel_chain)

res = final_chain.invoke({'topic': 'Human'})
print(res)