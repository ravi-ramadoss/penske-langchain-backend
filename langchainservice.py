from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

embeddings = OpenAIEmbeddings(  api_key=OPENAI_API_KEY)

index_name = "penske-rss"
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
retriever = vectorstore.as_retriever()
template = """Answer the question based only on the following context:


{context}

Question: {question}
"""
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template(template)
chain = (
    {"context": retriever , "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

def get_response(question):
    return chain.invoke(question)

