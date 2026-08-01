from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Quote the following joke and then explain it in minimum words\n{content}',
    input_variables=['content']
)

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

topic = input('Enter a topic: ')

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':topic}))
chain.get_graph().print_ascii()