from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite') 

prompt1 = PromptTemplate(
    template='Generate a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke in minium words\n{content}',
    input_variables=['content']
)

parser = StrOutputParser()

topic = input('Enter a topic: ')

initial_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'content': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(initial_chain, parallel_chain)

result = final_chain.invoke({'topic': topic})

print(result)
final_chain.get_graph().print_ascii()