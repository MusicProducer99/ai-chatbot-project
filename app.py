import streamlit as st
import anthropic 
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

st.title("Claude Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.messages.append({"role":"user","content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.messages.create(
        model= "claude-opus-4-6",
        max_tokens=1024,
        messages=st.session_state.messages
    )
    assistant_message= response.content[0].text
    st.session_state.messages.append({"role":"assistant","content": assistant_message})
    with st.chat_message("assistant"):
        st.write(assistant_message)


