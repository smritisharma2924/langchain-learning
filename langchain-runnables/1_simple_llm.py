from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

prompt = PromptTemplate(
    template="""Generate exactly two catchy blog titles for the topic {topic}, that are completely different from each other.' \
    'Rules:
    - Return only the two titles.
    - One title per line.
    - Do not use numbering or bullet points.
    - Do not add any introduction or explanation.""",
    input_variables=['topic']
)

parser = StrOutputParser()

topic = input('Enter a topic: ')

formatted_prompt = prompt.format(topic = topic)

result = model.invoke(formatted_prompt)

parsed_result = parser.invoke(result)

print(parsed_result)