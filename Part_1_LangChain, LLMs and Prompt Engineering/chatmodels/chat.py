from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import init_chat_model

# from langchain_openai import ChatOpenAI

# model = init_chat_model("gpt-4.1")
# model = ChatOpenAI(model = "gpt-5")
# response = model.invoke("what is cricket?")

# print(model)
# print(response.content)

# For Gemini

from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

# model = init_chat_model("google_genai:gemini-2.5-flash-lite")
# response = model.invoke("give me a para of 50 words on ml?")

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
# response = model.invoke("give me a para of 50 words on ml?")

# print(response.content)

# For Groq

# from langchain_groq import ChatGroq

# model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")
# response = model.invoke("give me a para of 50 words on ml?")

# print(response.content)

# For Mistral

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.7,
)
response = model.invoke("give me a para of 50 words on ml?")
print(response.content)
