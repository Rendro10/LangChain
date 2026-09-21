from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    'C:\\Users\\114-user\\OneDrive\\Desktop\\LangChain\\RAG\\document_loader\\books', 
    glob='*.pdf', 
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# print(type(docs))
# print(len(docs))

# print(docs[0].page_content)
# print(docs[0].metadata)

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)