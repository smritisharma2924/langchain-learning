# # Simple TypedDict

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from typing import TypedDict

# load_dotenv()

# model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

# #schema
# class Review(TypedDict):
#     summary: str
#     sentiment: str

# # Passes the Review schema to the model so it returns output in this structure without adding it manually to the prompt
# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

# print(result)
# print(result['summary'])
# print(result['sentiment'])



# # Annotated TypedDict
# # Annotated lets us attach descriptions to each field so the LLM understands what information should be generated for that field.

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from typing import TypedDict, Annotated

# load_dotenv()

# model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

# #schema
# # Define the expected structure of the LLM output.
# #  Annotated[type, description] specifies both the field's data type and instructions describing what the LLM should put in that field.
# class Review(TypedDict):
#     key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
#     summary: Annotated[str, "A brief summary of the review"]
#     sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]
#     pros: Annotated[list[str], "Write down all the pros summarized inside a list"]
#     cons: Annotated[list[str], "Write down all the cons summarized inside a list"]



# # Pass the schema, including the Annotated field descriptions, to the model. This guides the model to return data matching the Review structure.
# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse!
# The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos.
# The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often.
# What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light.
# Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
# However, the weight and size make it a bit uncomfortable for one-handed use.
# Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides?
# The $1,300 price tag is also a hard pill to swallow.
# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful
# Cons:
# Bulky and heavy-not great for one-handed use
# Bloatware still exists in One UI
# Expensive compared to competitors""")

# print(result)
