from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
chat_history = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurateanswers to user queries."),
]

while True:
    user_input=input('You :')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print('Bot :',response.content)
