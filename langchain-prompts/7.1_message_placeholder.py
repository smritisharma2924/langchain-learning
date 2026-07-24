from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'), #system message
    MessagesPlaceholder(variable_name = 'chat_history'), #to give the chatbot previous context
    ('human', '{query}') #current query, to be asked by the user
])

chat_history = []

#load chat history
with open('7.0_chathistory.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompt
prompt = chat_template.invoke({'chat_history' : chat_history, 'query' : 'Where is my refund'})

print(prompt)