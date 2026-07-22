print("1")

from langchain_google_genai import GoogleGenerativeAIEmbeddings
print("2")

from dotenv import load_dotenv
print("3")

load_dotenv()
print("4")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)
print("5")

result = embeddings.embed_query("What is the capital of India?")
print("6")

print(result)

# print("A")
# import google.genai
# print("B")