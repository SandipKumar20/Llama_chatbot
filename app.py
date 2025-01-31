import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="Llama 3 Chatbot", page_icon="🤖", layout="wide")

st.title("🦙 Llama 3.2:1B Chatbot using Ollama & Streamlit")
st.markdown("Chat with Llama 3.2:1B model powered by Ollama API.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user messages
user_input = st.chat_input("Type your message...")

# Ollama API function
OLLAMA_URL = "http://localhost:11434/api/generate"

def get_llama_response(prompt):
    payload = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Process user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Llama response
    response = get_llama_response(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)

    # Append response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})