Here is a summary of Video 13 on **Retrievers in LangChain** by CampusX for quick revision:

---

### **1. What is a Retriever?**

* An interface that returns documents given an un-structured query.
* It wraps around vector stores (or other data sources) to fetch relevant context for Retrieval Augmented Generation (RAG) pipelines.
* **Key Difference vs. Similarity Search:** Similarity search simply calculates vector distance to find nearest matches, whereas retrievers apply search strategies (like filtering, re-ranking, query expansion, or compression) to optimize context quality.

---

### **2. Core Types of Retrievers**

#### **A. Vector Store Retriever**

* Uses a standard vector store index to search for documents based on cosine similarity or distance metrics.

#### **B. Maximal Marginal Relevance (MMR) Retriever**

* **Problem Solved:** Prevents retrieving redundant documents that repeat the same information.
* **How it Works:**
1. Selects the most relevant document first.
2. Selects subsequent documents that are relevant to the query but least similar to already chosen documents.


* **Best Used For:** Diversity in context windows when dealing with semantically overlapping documents.

#### **C. Multi-Query Retriever**

* **Problem Solved:** Users often write poorly phrased or ambiguous queries.
* **How it Works:** Uses an LLM to automatically generate multiple variations of the user's input query, runs similarity search for each variation, and combines the unique retrieved documents.
* **Best Used For:** Improving recall and overcoming prompt phrasing limitations.

#### **D. Contextual Compression Retriever**

* **Problem Solved:** Document chunks often contain extra irrelevant text along with the answer, clogging the LLM context window.
* **How it Works:** Uses a document compressor (such as `LLMChainExtractor`) to extract only the relevant snippet from each retrieved document before returning it.
* **Best Used For:** Saving tokens and focusing the model on exact, pertinent details.

---

### **3. Key Takeaways for RAG**

* **Text Splitter Impact:** Bad chunking leads to noisy retrievals; combining proper text splitting with advanced retrievers ensures high precision.
* **Retrieval Strategy Selection:** Choose MMR for diversity, Multi-Query for broader coverage, and Contextual Compression to minimize context length.