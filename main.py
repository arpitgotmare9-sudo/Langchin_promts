from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
# Made the model object
model=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    max_tokens=100
)
st.header("Chatbot!")

user_input=st.text_input("Enter the promt")

# Output with the button
if st.button("💡"):
    result=model.invoke(user_input)
    st.write(result.content)
