from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Load the model
llm = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

# Create a prompt template
prompt = PromptTemplate(
    template="Suggest a single catchy blog title about {topic}",
    input_variables=['topic']
)

# Parser
parser = StrOutputParser()

# Create an llmchain
chain = prompt | llm | parser

# Run the chain with a specific topic
topic = input("Enter a topic: ")
output = chain.invoke({'topic':topic})

print("Generated Blog Title: ", output)