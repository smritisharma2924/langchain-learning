from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI : ", result.content)

print("Thank you for using.")
print(chat_history)

# here the problem is that we dont know by seeing the chat_history that a particular message is sent by user or the assistant
# langchain identified this problem and created built in classes.