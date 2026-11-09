from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

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