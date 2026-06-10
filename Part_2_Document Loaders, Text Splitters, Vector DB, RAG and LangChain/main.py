from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

# data = TextLoader("documentLoaders/notes.txt")
loader = PyPDFLoader("documentLoaders/GRU.pdf")
docs = loader.load()

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes the text."),
    ("human", "{text}")
])

prompt = prompt_template.format_messages(
    text = docs[0].page_content
)

model = ChatMistralAI(model="mistral-small-2506")

result = model.invoke(prompt)

print(result.content)