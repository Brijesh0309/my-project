# rag_app.py
# Streamlit RAG Chatbot UI

import streamlit as st
from langchain.chains import RetrievalQA

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.llms import Ollama


# ---------------------------
# STREAMLIT UI TITLE
# ---------------------------

st.title("📚 RAG Chatbot with Streamlit")
st.write("Ask questions from your document.")

# ---------------------------
# LOAD DOCUMENT
# ---------------------------

loader = TextLoader("C:/Users/admin/PythonProjects/ra_app/data.txt")
documents = loader.load()

# ---------------------------
# SPLIT DOCUMENT
# ---------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs_split = splitter.split_documents(documents)

# ---------------------------
# CREATE EMBEDDINGS
# ---------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------
# VECTOR DATABASE
# ---------------------------

vectorstore = FAISS.from_documents(
    docs_split,
    embeddings
)

retriever = vectorstore.as_retriever()

# ---------------------------
# LLM MODEL
# ---------------------------

llm = Ollama(model="llama2")

# ---------------------------
# RAG CHAIN
# ---------------------------

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# ---------------------------
# CHAT UI
# ---------------------------

user_question = st.text_input("Ask a question from the document")

if user_question:

    response = qa.run(user_question)

    st.write("### 🤖 Answer")
    st.write(response)