from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path

script_dir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=script_dir / "env.env")


model=ChatGroq(
    model="openai/gpt-oss-120b"
)

message=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about the Langchain')
]

result=model.invoke(message)


message.append(AIMessage(content=result.content))

print(message)