from typing import Annotated

import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import InjectedToolArg, tool
from langchain_openai import ChatOpenAI

# Loads OPENAI_API_KEY from your .env file (ChatOpenAI reads it automatically)
load_dotenv()

# ExchangeRate-API key, set directly in the code
EXCHANGE_RATE_API_KEY = "paste_your_exchangerate_api_key_here"


# --------------------------------------------------
# Tool 1: Get conversion factor
# --------------------------------------------------

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    Fetch the currency conversion factor between
    a base currency and a target currency.
    """
    url = (
        f"https://v6.exchangerate-api.com/v6/"
        f"be0c8aca5c7a779beb825cd2/latest/{base_currency.upper()}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data["conversion_rates"][target_currency.upper()]


# --------------------------------------------------
# Tool 2: Convert currency
# --------------------------------------------------
# conversion_rate is InjectedToolArg: the LLM does NOT generate it,
# we inject it at runtime after get_conversion_factor has run.

@tool
def convert(
    base_currency_value: float,
    conversion_rate: Annotated[float, InjectedToolArg],
) -> float:
    """
    Calculate target currency value.
    """
    return base_currency_value * conversion_rate


# --------------------------------------------------
# Create LLM and bind tools
# --------------------------------------------------

llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools([get_conversion_factor, convert])


# --------------------------------------------------
# User message
# --------------------------------------------------

messages = [
    HumanMessage(
        content=(
            "What is the conversion factor between USD and INR, "
            "and convert 10 USD to INR."
        )
    )
]


# --------------------------------------------------
# First LLM call
# --------------------------------------------------

ai_message = llm_with_tools.invoke(messages)

print("\nAI message:")
print(ai_message)

print("\nTool calls:")
print(ai_message.tool_calls)

# IMPORTANT: add the AI message containing tool_calls
messages.append(ai_message)


# --------------------------------------------------
# Execute tool calls
# --------------------------------------------------
# Run get_conversion_factor first so the rate is available to inject
# into convert, regardless of the order the model listed them in.

ordered_calls = sorted(
    ai_message.tool_calls,
    key=lambda call: 0 if call["name"] == "get_conversion_factor" else 1,
)

conversion_rate = None

for tool_call in ordered_calls:
    tool_name = tool_call["name"]
    tool_args = dict(tool_call["args"])
    tool_call_id = tool_call["id"]

    print("\nTool name:", tool_name)
    print("Tool args:", tool_args)

    if tool_name == "get_conversion_factor":
        result = get_conversion_factor.invoke(tool_args)
        conversion_rate = result  # save for the convert tool

    elif tool_name == "convert":
        if conversion_rate is None:
            raise ValueError(
                "convert was called but no conversion rate is available. "
                "get_conversion_factor must be called first."
            )
        tool_args["conversion_rate"] = conversion_rate  # inject it
        result = convert.invoke(tool_args)

    else:
        raise ValueError(f"Unknown tool: {tool_name}")

    print("Tool result:", result)

    # IMPORTANT: every tool_call MUST have a matching ToolMessage
    messages.append(
        ToolMessage(
            content=str(result),
            tool_call_id=tool_call_id,
        )
    )


# --------------------------------------------------
# Second LLM call
# --------------------------------------------------

final_response = llm_with_tools.invoke(messages)

print("\nFinal response:")
print(final_response.content)