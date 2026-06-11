from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


data = PyPDFLoader("documentLoaders/GRU.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)

# contains page content and meta data both
# print(len(docs))
# print(docs[14]) 

print(len(chunks))
print(chunks[0].page_content)