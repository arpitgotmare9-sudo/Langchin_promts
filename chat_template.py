from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple words, What is {topic}')
])

promt=chat_template.invoke({'domain':'football','topic':'offside'})

print(promt)