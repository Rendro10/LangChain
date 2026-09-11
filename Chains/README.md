**1. What are Chains?**

* Chains allow you to link multiple components together (e.g., Prompt Templates, Models, and Output Parsers) into a single, cohesive processing pipeline.
* Rather than running each step manually, chains automatically pass the output of one step as the input to the next using standard LangChain Expression Language (LCEL) pipe syntax (`|`).

---

**2. Key Types of Chains**

| Chain Type | Description | Primary Use Case |
| --- | --- | --- |
| **Simple Chain** | Connects a single prompt, LLM model, and output parser in a linear flow (`prompt | model | parser`). | Basic single-prompt generation tasks (e.g., generating facts or quick summaries). |
| **Sequential Chain** | Runs multiple steps one after another; the output of one sub-chain becomes the input to the next chain. | Multi-stage text generation (e.g., generating a long document, then extracting a bulleted summary from it). |
| **Parallel Chain** | Runs multiple independent chains simultaneously on the same input using `RunnableParallel`. | Multi-task generation on a single context (e.g., generating lecture notes and a quiz concurrently from the same text). |
| **Conditional Chain** | Evaluates input conditions using `RunnableBranch` or `RunnableLambda` to route execution to specific sub-chains. | Dynamic decision routing (e.g., classifying user feedback sentiment to send a positive, negative, or neutral response). |

---

**3. Key Implementation Components**

* **LCEL Composition:** Modern LangChain uses pipe syntax (`|`) to streamline chain creation without relying on legacy `LLMChain` classes.
* **`RunnableParallel`:** Wraps a dictionary of chains to execute them concurrently and return a combined dictionary of results.
* **`RunnableBranch`:** Takes tuples of conditions and target chains `(condition_fn, target_chain)` along with a default fallback chain for conditional logic.