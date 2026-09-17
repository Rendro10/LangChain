from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableBranch
load_dotenv()


prompt1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables = ['topic'],
)

prompt2 = PromptTemplate(
    template = 'summarise the following {text}',
    input_variables = ['text'],
)

model = ChatOpenAI()
parser = StrOutputParser()

report_generation_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generation_chain, branch_chain)

result = final_chain.invoke({'topic':'AI'})

print(result)

