from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2"
)
documents = [
    "Delhi is the capital of India.",
    "Paris is the captial of France.",
    "Kolkata is the capital of West Bengal."
]

result = embeddings.embed_documents(documents)

print(result)
