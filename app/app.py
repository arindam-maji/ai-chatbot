import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot")

user_input = st.text_input("You: ", "")

if user_input:
    response = get_response(user_input)
    st.write(f"Bot: {response}")
