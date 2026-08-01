from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

parser = StrOutputParser()

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

topic = input('Enter a topic: ')

sequence_chain = RunnableSequence(prompt, model, parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'count': runnable_word_counter
})

final_chain = RunnableSequence(sequence_chain, parallel_chain)
print(final_chain.invoke({'topic': topic}))
final_chain.get_graph().print_ascii()