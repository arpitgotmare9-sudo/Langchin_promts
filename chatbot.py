from pathlib import Path

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")

model=ChatGroq(model="openai/gpt-oss-120b")

chat_history=[
    SystemMessage(content=''),
    HumanMessage(content='')
]


while True:
    user_input=input("You: ")
    if user_input=='exit':
        break
    else:
        template=load_prompt(str(script_dir / 'template1.json'))
        chat_history.append(user_input)
        promt=template.invoke({
            'question':chat_history
        })
        result=model.invoke(promt)
        chat_history.append(AIMessage(content=result.content))
        print(result.content)
print(chat_history)