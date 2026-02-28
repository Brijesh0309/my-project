# rag_app.py - Compatible with LangChain v1.2.10

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1️⃣ Load the text file
loader = TextLoader("C:/Users/admin/PythonProjects/ra_app/data.txt")
documents = loader.load()

print(f"Loaded {len(documents)} document(s).")

# 2️⃣ Split documents into smaller chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs_split = splitter.split_documents(documents)
print(f"Split into {len(docs_split)} chunks.")

# 3️⃣ Print first few chunks
for i, doc in enumerate(docs_split[:5]):
    print(f"\n--- Chunk {i+1} ---")
    print(doc.page_content)