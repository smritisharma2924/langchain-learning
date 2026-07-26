# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id = "Qwen/Qwen2.5-7B-Instruct",
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm = llm)

# # list of schema objects
# schema = [
#     ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic'),
#     ResponseSchema(name = 'fact_2', description = 'Fact 2 about the topic'),
#     ResponseSchema(name = 'fact_3', description = 'Fact 3 about the topic')
# ]

# parser = StructuredOutputParser.from_response_schemas(schema)

# template = PromptTemplate(
#     template = 'Give 3 facts about the {topic} \n {format_instruction}',
#     input_variables = ['topic'],
#     partial_variables = {'format_instruction' : parser.get_format_instructions()}
# )

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
# print(final_result)




# NOTE:
# StructuredOutputParser and ResponseSchema are legacy LangChain APIs
# shown in older tutorials and are not available at this import path
# in the current LangChain version.
#
# Concept: They allowed us to define expected output fields and their
# descriptions, improving on a basic JsonOutputParser.
#
# In modern LangChain, prefer with_structured_output() with
# TypedDict, Pydantic, or JSON Schema.