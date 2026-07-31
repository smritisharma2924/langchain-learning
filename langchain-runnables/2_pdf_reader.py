# pdf load -> split -> embed -> vectorstore -> retrieve -> llm -> parse -> output

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Load the document
loader = TextLoader("docs.txt") #ensure docs.txt exist
documents = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Convert text into embeddings & store in FAISS
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2"
)
vectorstore = FAISS.from_documents(docs, embeddings)

# Create a retriever (fetches relevant documents)
retriever = vectorstore.as_retriever()

# Manually retrieve relevant documents
query = "what are the key takeaways from the documents?"
retrieved_docs = retriever._get_relevant_documents(query)

# Combine retrived text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# initialize the llm
llm = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')

# Manually pass the retrieved text to llm
prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)

# print the answer
print("Anwer:", answer)