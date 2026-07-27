from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
model2 = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')
model3 = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1 = PromptTemplate(
    template='Generate short and simple notes on the topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a quiz of 5 short questions with solutions on the topic {topic}',
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n {notes} \n {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model3 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'topic':'Neural Networks'})
print(result)

chain.get_graph().print_ascii()