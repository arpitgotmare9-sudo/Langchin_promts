from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
from langchain_core.prompts import PromptTemplate

load_dotenv()
# Made the model object
model=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    max_tokens=500
)
st.header("Chatbot 🤖")
# For dynamic promt 
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template=load_prompt('template.json')
promt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

# Output with the button
if st.button("💡"):
    #result=model.invoke(user_input)
    result=model.invoke(promt)
    st.write(result.content)
