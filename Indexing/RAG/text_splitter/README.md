**Core Concept: Text Splitting (Chunking)**

* **Role in RAG:** Breaks large documents into smaller, manageable chunks before generating embeddings and storing them in vector databases.
* **Key Challenge:** Balancing chunk size—chunks that are too large exceed LLM context windows or add noise, while chunks that are too small lose crucial context.

**4 Main Types of Text Splitters**

1. **Length-Based Splitting**
* **Mechanism:** Splits text strictly by character count or token length (e.g., using `CharacterTextSplitter`).
* **Limitation:** Can cut sentences mid-way or separate related ideas, leading to loss of semantic coherence.


2. **Structure-Based / Document-Specific Splitting**
* **Mechanism:** Leverages document syntax or markup rules (e.g., Markdown headers, HTML tags, Python code structures) to define split points.
* **Advantage:** Preserves natural document hierarchies and code block integrity.


3. **Recursive Character Splitting**
* **Mechanism:** Uses a hierarchy of separators (e.g., `["\n\n", "\n", " ", ""]`) to recursively divide text into target chunk sizes (`RecursiveCharacterTextSplitter`).
* **Advantage:** Standard baseline approach in LangChain because it attempts to keep paragraphs and sentences intact before splitting further.


4. **Semantic Meaning-Based Splitting**
* **Mechanism:** Uses an embedding model to evaluate cosine similarity between adjacent sentences ($S_1, S_2, S_3, \dots, S_n$).
* **Process:** Splits text where semantic similarity drops significantly below a defined threshold, grouping topic-related sentences together regardless of paragraph or structural boundaries.