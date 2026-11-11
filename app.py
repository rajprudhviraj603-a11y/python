
import streamlit as st
from ollama import Client

# Connect to Ollama
client = Client(host="http://localhost:11434")

# Page configuration
st.set_page_config(
    page_title="Custom LLM Model by Prudhvi Raju - Ollama",
    layout="centered"
)

# App title
st.title("Mr. Prudhvi Raju - Ollama App")

# User prompt
prompt = st.text_area(
    "Enter your prompt:",
    height=200
)

# Generate response
if st.button("Generate Response"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="deepseek-r1:1.5b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("Response Generated!")
        st.write(response["message"]["content"])

