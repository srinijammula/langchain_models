from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()
model = HuggingFaceEndpointEmbeddings(repo_id="sentence-transformers/all-MiniLM-L6-v2")
docs=["What is the capital of France?", 
        "What is the capital of Germany?",
        "What is the capital of Italy?"]
response = model.embed_query("What is the capital of France?")  
response2 = model.embed_documents(docs)
print(response2)