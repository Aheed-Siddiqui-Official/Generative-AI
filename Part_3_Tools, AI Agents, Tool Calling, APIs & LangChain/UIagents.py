import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
from tavily import TavilyClient

# ====================== TOOLS ======================

@tool
def get_weather(city: str) -> str:
    """Get current weather of a city"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Error: OPENWEATHER_API_KEY not found in .env"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if str(data.get("cod")) != "200":
        return f"Error: {data.get('message', 'Could not fetch weather')}"
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"Weather in {city}: {desc}, {temp}°C"


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city: str) -> str:
    """Get latest news about a city"""
    response = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=5
    )
    results = response.get("results", [])
    
    if not results:
        return f"No news found for {city}"
    
    news_list = [
        f"- **{r.get('title', 'No title')}**\n  🔗 {r.get('url', '')}\n  📝 {r.get('content', '')[:150]}..."
        for r in results
    ]
    return f"**Latest news in {city}:**\n\n" + "\n\n".join(news_list)


# ====================== LLM ======================
llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.7,
    max_tokens=1000
)

tools = [get_weather, get_news]
llm_with_tools = llm.bind_tools(tools)


# ====================== STREAMLIT UI ======================
st.set_page_config(page_title="City Intelligence Assistant", page_icon="🏙️")
st.title("🏙️ City Intelligence System")
st.caption("Ask about weather or latest news of any city")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your city assistant. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# User input
if prompt := st.chat_input("Type your message here... (e.g. weather in Bhopal)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Prepare messages for LLM
    messages = [HumanMessage(content=m["content"]) if m["role"] == "user" 
                else AIMessage(content=m["content"]) 
                for m in st.session_state.messages]

    # First LLM call
    with st.spinner("Thinking..."):
        ai_response = llm_with_tools.invoke(messages)
        messages.append(ai_response)

        # Handle tool calls with human approval
        if ai_response.tool_calls:
            for tool_call in ai_response.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                
                # Human Approval
                approve = st.radio(
                    f"Agent wants to call **{tool_name}** with args: `{tool_args}`",
                    options=["Yes", "No"],
                    horizontal=True,
                    key=f"approve_{len(st.session_state.messages)}"
                )
                
                if approve == "No":
                    tool_output = "Tool call denied by user."
                else:
                    # Execute tool
                    if tool_name == "get_weather":
                        tool_output = get_weather.invoke(tool_args)
                    elif tool_name == "get_news":
                        tool_output = get_news.invoke(tool_args)
                    else:
                        tool_output = "Unknown tool"

                # Add tool response
                messages.append(ToolMessage(
                    content=str(tool_output),
                    tool_call_id=tool_call["id"]
                ))

            # Final LLM call after tool results
            final_response = llm_with_tools.invoke(messages)
            final_content = final_response.content
        else:
            final_content = ai_response.content

        # Display final response
        st.chat_message("assistant").write(final_content)
        st.session_state.messages.append({"role": "assistant", "content": final_content})