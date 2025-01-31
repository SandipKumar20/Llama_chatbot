import streamlit as st
import ollama


def generate_response(prompt):
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]


def main():
    st.title("Chat with Llama")
    prompt = st.text_area("Enter your prompt: ")

    if st.button("Generate Response"):
        if prompt:
            with st.spinner("Generating response..."):
                response = generate_response(prompt)
                st.write("**Response:**")
                st.write(response)
        else:
            st.warning("Please enter a prompt to get a response.")

if __name__ == "__main__":
    main()       