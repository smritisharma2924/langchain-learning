# topic -> llm -> report -> llm -> summary

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on the topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Extract the 5 most important facts in 1 line each from the following report \n {report}',
    input_variables=['report']
)

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'unemployment in india'})
print(result)
chain.get_graph().print_ascii()