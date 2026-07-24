from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

chat_history = [
    SystemMessage(content = "You are a helpful AI Assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.text))
    print("AI : ", result.text)

print("Thank you for using.")
print(chat_history)
