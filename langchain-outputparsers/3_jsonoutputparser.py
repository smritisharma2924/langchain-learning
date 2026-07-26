from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

# JsonOutputParser:
# - Instructs the LLM to generate valid JSON and parses that JSON into a Python object (usually a dict).
# - Unlike StrOutputParser, it does not just extract text; it converts JSON-formatted model output into structured Python data.
parser = JsonOutputParser()



# get_format_instructions() generates instructions telling the LLM how its response should be formatted so that JsonOutputParser can parse it.
# partial_variables is used because format_instruction is fixed and does not need to be supplied every time the chain is invoked.
template = PromptTemplate(
    template = "Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# print(prompt)

# result = model.invoke(prompt)
# print(result)

# final_result = parser.parse(result.content)


# LCEL pipeline: PromptTemplate -> Model -> AIMessage -> JsonOutputParser -> Python dict
chain = template | model | parser

final_result = chain.invoke({})
print(final_result)

# Limitation of JsonOutputParser:
# It can parse JSON output into Python objects, but without a schema it does not strictly enforce the required fields, data types, or validation rules.
# For strict structured output and validation, Pydantic is generally preferred.