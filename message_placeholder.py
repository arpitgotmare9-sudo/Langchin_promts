from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
# chat template

chat_template=ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{querry}') 
])

# load chat history
chat_history=[]

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

# create prompt
promt=chat_template.invoke({'chat_history': chat_history,'querry': HumanMessage(content='Where is my refund')})

print(promt)