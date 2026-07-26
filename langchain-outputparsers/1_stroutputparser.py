# why do we need string output parser if it only converts the output into string? we can do the same using .content function too...
# ex: we need to first ask for a detailed explanation to the llm and then give the generated text again to the llm and asking for 5 lines summary.
# lets see how both perform- .content and strOutputParser. this file contains the first one

# gemini can also be useed here
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

# 1st prompt -> detailed explanation
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic']
)

# 2nd prompt -> summary in 5 lines
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. /n {text}',
    input_variables = ['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result1 = model.invoke(prompt1)

# manually extract string
prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)

# manually extract string again
print(result2.content)