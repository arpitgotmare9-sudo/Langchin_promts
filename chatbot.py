from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b")

while True:
    user_input=input("You: ")
    if user_input=='exit':
        break
    else:
        template=load_prompt('template1.json')
        promt=template.invoke({
            'question':user_input
        })
        result=model.invoke(promt)
        print(result.content)

