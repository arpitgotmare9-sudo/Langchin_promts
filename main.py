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
st.header("Chatbot 🤖")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#template = load_prompt('template.json')

# Output with the button
if st.button("💡"):
    #result=model.invoke(user_input)
    st.write(".....")
