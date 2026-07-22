from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-2", dimensions = 300)

document = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Crisket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = input("Enter your query :")

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] #to get 1d list instead of 2d
index, score = sorted(list(enumerate(scores)), key = lambda x:x[1], reverse = True)[0]

print(query)
print(document[index])
print("Similarity score is : ", score)