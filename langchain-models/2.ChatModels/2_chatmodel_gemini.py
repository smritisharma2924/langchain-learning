from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash', temperature = 1.8, max_output_tokens = 2000)

result = model.invoke("Who is Olivia Rodrigo?")

print(result.content)