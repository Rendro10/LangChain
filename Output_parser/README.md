**1. What are Output Parsers?**

* Tools in LangChain designed to structure, extract, and format raw unstructured string outputs from LLMs into usable data formats (e.g., Python strings, JSON, or Pydantic objects).
* Primary bridge when model responses need to feed into databases, APIs, or downstream application logic.

**2. Why Use Output Parsers?**

* **LLM Model Compatibility:** While models with native function-calling support can use `with_structured_output()`, models without native support rely on output parsers to structure responses via prompt instruction and post-processing.
* **Chain Integration:** Output parsers work seamlessly inside LangChain chains (`|` syntax) to automate response transformation.

---

**3. Comparison of Key Output Parsers**

| Parser Type | Purpose / Output Format | Key Characteristics | Limitations / Best Used For |
| --- | --- | --- | --- |
| **`StrOutputParser`** | Plain String (`str`) | Extracts the text content directly from model outputs. | Ideal for simple text-based chains without structural requirements. |
| **`JsonOutputParser`** | JSON / Python `dict` | Instructs model to output valid JSON format. | Output structure is decided by the LLM; no strict schema or typing rules enforced. |
| **`StructuredOutputParser`** | Structured JSON | Uses field schemas to enforce key names and formats. | Flexible formatting, but lacks runtime type validation. *(Note: Deprecated/removed in newer LangChain versions)* |
| **`PydanticOutputParser`** | Pydantic Schema | Enforces strict schema, type safety, field constraints, and runtime validation. | Best choice for complex schemas requiring strict type checking and validation errors. |

---

**4. Execution Flow**

* **Format Instructions:** Parsers generate string-based formatting instructions via `.get_format_instructions()` that are appended directly to prompt templates.
* **Inference & Parsing:** The LLM receives the instructions, generates the text response, and passes it through the parser's `.parse()` method to extract the final structured object.