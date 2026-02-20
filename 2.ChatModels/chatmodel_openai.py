from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4o")
response = model.invoke("tell joke",temperature=1.9)
print(response.content)