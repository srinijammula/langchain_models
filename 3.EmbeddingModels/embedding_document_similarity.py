from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
model = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32) 
docs=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="Who is aggressive Indian cricketer and leader?"
query_embedding = model.embed_query(query)
doc_embeddings = model.embed_documents(docs)
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]  
print(similarities)
most_similar_doc_index = np.argmax(similarities)
print("Most similar document:", docs[most_similar_doc_index])