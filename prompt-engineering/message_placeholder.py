from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ("system", "You are a customer support agent"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{user_input}"),      
])

chat_history=[]
with open('chat_history.txt', 'r') as f:
    for line in f:
        chat_history.append(line.strip())

#create prompt
prompt = chat_template.invoke({'history': chat_history, 'user_input': "Where is my refund?"})

print(prompt)