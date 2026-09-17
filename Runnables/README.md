**1. What are Runnables?**

* **LangChain Interface:** A fundamental protocol in LangChain (part of LCEL - LangChain Expression Language) that gives components a standardized, unified interface for execution.
* **Unified Workflow:** Converts various isolated components—such as Prompts, LLMs, Output Parsers, and custom functions—into predictable, chainable objects that support common execution paradigms out of the box.

---

**2. Key Executable Methods**

| Method | Purpose | Execution Style |
| --- | --- | --- |
| **`.invoke()`** | Process a single input and return a single response synchronously. | Standard call (e.g., `chain.invoke({"topic": "AI"})`) |
| **`.stream()`** | Stream back chunks of the response as they are generated in real-time. | Useful for responsive UI generation (e.g., streaming LLM output tokens) |
| **`.batch()`** | Process a list or array of inputs concurrently in parallel. | Efficient for multi-input workflows without looping manually |
| **`a-` variants** | Async versions of the methods (`.ainvoke()`, `.astream()`, `.abatch()`). | Non-blocking execution for web frameworks (e.g., FastAPI, AsyncIO) |

---

**3. Essential Core Runnable Types**

* **`RunnableSequence`:**
* Created implicitly when chaining components using the pipe operator (`|`).
* Passes the output of component $A$ directly into component $B$ ($A \rightarrow B$).


* **`RunnableParallel`:**
* Runs multiple runnables simultaneously on the same input data using Python dictionaries.
* Combines outputs into a unified dictionary structure.


* **`RunnablePassthrough`:**
* Passes input data through unmodified or allows adding additional key-value fields to the inputs entering downstream steps.


* **`RunnableLambda`:**
* Wraps custom Python functions (e.g., text cleaning, custom formatting logic) to make them compliant with the LCEL interface and pipe syntax (`|`).


* **`RunnableBranch`:**
* Enables conditional routing by evaluating inputs against specific conditions and directing execution to corresponding sub-chains.