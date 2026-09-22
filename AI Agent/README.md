## **1. What is a Tool?**

A **tool** in LangChain is a Python function (or API) packaged in a specific format so an LLM can understand, choose, and execute it when needed.

* **LLMs (e.g., GPT, Claude) are great at:**
* Reasoning & decision-making
* Text generation & language processing


* **LLMs cannot inherently:**
* Access live/real-time data (e.g., weather, live stock prices, news)
* Perform exact or complex calculations reliably
* Execute external code or scripts
* Make API calls or query databases directly



> **Key Takeaway:** Tools bridge the gap between an LLM's reasoning capabilities and real-world actions or external dynamic data sources.

---

## **2. Standard / Built-in Tools in LangChain**

LangChain provides pre-built integrations for common utilities that can be loaded directly:

* **Search Tools:** `DuckDuckGoSearchRun`, `TavilySearchResults`, Google Search APIs (for web search).
* **Code Execution:** Python REPL (`PythonAstREPLTool`) to execute code dynamically.
* **Math/Computation:** `LLMMathChain` or specific calculation utilities for precise arithmetic.
* **Database & File Systems:** SQL Database tools, Wikipedia tools, File reading/writing utilities.

---

## **3. Creating Custom Tools in LangChain**

When standard tools don't cover a use case, custom tools can be created using several approaches:

### **A. Using the `@tool` Decorator (Recommended & Simplest)**

* Decorate a standard Python function with `@tool`.
* Provide clear **type hints** for inputs and outputs.
* Write a detailed **docstring**—the LLM reads this docstring to understand *when* and *how* to invoke the tool.

### **B. Subclassing `BaseTool**`

* Useful for complex, object-oriented tool creation.
* Defines explicit schema models (`args_schema`) using Pydantic.
* Overrides `_run` (synchronous execution) and optional `_arun` (asynchronous execution).

---

## **4. Key Components of a Tool Schema**

For an LLM to call a tool accurately, three components must be clear:

1. **Name:** A clean, identifier-style name (e.g., `get_weather_data`).
2. **Description:** Clear explanation of what the tool does and under what conditions it should be called.
3. **Arguments / Input Schema:** Defined via type annotations or Pydantic models specifying required parameters.

---

## **5. How LLMs Use Tools (The Tool Execution Flow)**

1. **User Query:** User sends a prompt (e.g., *"What is the weather in Delhi right now?"*).
2. **Tool Selection:** The LLM inspects available tools and decides if any tool is needed.
3. **Function Call Request:** The LLM returns a structured request with tool name and arguments.
4. **Execution:** LangChain executes the underlying Python function using those arguments.
5. **Final Output:** The tool result is passed back to the LLM to format a final, natural-language response for the user.