4 Majore components of RAG are: Document loader, text splitter, embedding to vector and stroring it to vectorDB, and fetching through retrival


**Document Loaders**

Document Loaders serve as the first pipeline component in Retrieval-Augmented Generation (RAG) systems using LangChain, converting diverse unstructured or structured data formats into standard `Document` objects.

**Core Concept & RAG Architecture**

* **Role in RAG:** Serves as the entry point for ingesting external data sources into the system before processing via Text Splitters, Vector Databases, and Retrievers.
* **Standardization:** Transforms diverse file formats (PDFs, text files, web pages, databases) into a standardized LangChain `Document` format.
* **Document Object Structure:**
* `page_content`: The raw text extract from the source data.
* `metadata`: Contextual details such as source path, file name, page numbers, or creation dates.



**Common Types of Document Loaders**

* **File Loaders:** For local files like text files (`TextLoader`), PDFs (`PyPDFLoader`, `UnstructuredPDFLoader`), or CSVs (`CSVLoader`).
* **Web Loaders:** Extract and parse content from websites or online sources (`WebBaseLoader`, `UnstructuredURLLoader`).
* **Directory Loaders:** For ingesting multiple files of varying formats simultaneously from a directory (`DirectoryLoader`).
* **Third-Party Service Loaders:** For directly loading data from cloud services like Google Drive, Notion, Slack, or databases.

**Key Operations**

* `.load()`: Synchronously loads and parses all documents into a list of `Document` objects in memory.
* `.lazy_load()`: Loads documents page-by-page or chunk-by-chunk using a generator to optimize memory when processing large datasets or memory-constrained environments.