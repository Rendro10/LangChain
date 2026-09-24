from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv


load_dotenv()

# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b


# print(multiply.invoke({'a':4, 'b':5}))

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)


llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([multiply])

# res = llm_with_tools.invoke('Hi how are you')
# print(res)

query = HumanMessage('can you multiply 3 with 9000')

messages = [query]
result = llm_with_tools.invoke(messages)
messages.append(result)

# print(messages)

tool_result = multiply.invoke(result.tool_calls[0])

# print(tool_result)

messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)


