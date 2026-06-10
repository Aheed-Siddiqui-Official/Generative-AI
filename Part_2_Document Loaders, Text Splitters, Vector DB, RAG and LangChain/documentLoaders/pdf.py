from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("documentLoaders/GRU.pdf")

docs = data.load()

# contains page content and meta data both
print(len(docs))
print(docs[14]) 