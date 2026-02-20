from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv      

load_dotenv()
model = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32) 
docs=["What is the capital of France?",
      "What is the capital of Germany?",
      "What is the capital of Italy?"]   
response = model.embed_query("What is the capital of France?")
response2 = model.embed_documents(docs)


print(response2)