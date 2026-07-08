from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash', temperature = 1.8, max_completion_tokens = 20)

result = model.invoke("List the songs of Olivia Rodrigo's new album 'you seem pretty sad for a girl so in love'.")

print(result.content)