# Static prompt version
# User input is passed directly to the model

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("AI Assistant")

user_input = st.text_input("Enter you prompt : ")
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

if st.button("Generate") :
    result = model.invoke(user_input)
    st.write(result.content)