import os
from dotenv import load_dotenv

import json
from pathlib import Path
import shutil
import hashlib
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Save
FAISS_INDEX_PATH = "vectorstores/legal_docs_index" #FAISS index path
HASH_INDEX_PATH = "vectorstores/hash_index.json"
ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
llm = ChatOllama(model="mistral", base_url=ollama_url)

load_dotenv()

# Creating embedding model once instead (Semantic search)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def is_duplicate(text_hash: str) -> bool:
    if not Path(HASH_INDEX_PATH).exists():
        return False
    with open(HASH_INDEX_PATH, "r") as f:
        known = json.load(f)["hashes"]
    return text_hash in known

def save_hash(text_hash: str):
    if Path(HASH_INDEX_PATH).exists():
        with open(HASH_INDEX_PATH, "r") as f:
            hashes = json.load(f)
    else:
        hashes = {"hashes": []}
    hashes["hashes"].append(text_hash)
    with open(HASH_INDEX_PATH, "w") as f:
        json.dump(hashes, f)


# Step 1: Upload & Store
def store_embeddings(text: str):
    text_hash = hash_text(text)
    if is_duplicate(text_hash):
        print("Duplicate document detected. Skipping reprocessing.")
        return "This document was already uploaded."

    #Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=600, separators=["\n\n", "\n", ".", " ", ""])
    chunks = splitter.create_documents([text])

    # Create FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(FAISS_INDEX_PATH) #save locally
    save_hash(text_hash)
    return "✅ Document processed and stored."


def query_index(question: str) -> str:
    if not os.path.exists(FAISS_INDEX_PATH):
        return "No document uploaded yet. Please upload first."

    vectorstore = FAISS.load_local(
        FAISS_INDEX_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 10, "fetch_k": 20})

    # Optional: Custom prompt
    prompt_template = """
    You're a legal assistant reading the following context:

    {context}

    Using ONLY the provided context, answer the question below as precisely as possible. If the answer is implied or partially addressed, explain that.

    Question:
    {question}
    """
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )

    result = qa_chain({"query": question})
    return result["result"]


def deleteVectorStore():
    if Path(FAISS_INDEX_PATH).exists():
        shutil.rmtree(FAISS_INDEX_PATH)

    with open(HASH_INDEX_PATH, "w") as f:
        json.dump({"hashes": []}, f)





# # Our main function: takes a document and a question, returns an answer
# def process_query(text: str, question: str) -> str:
#     # 1. Split text into chunks
#     splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
#     chunks = splitter.create_documents([text])
#
#     # 2. Load local LLM
#     llm = ChatOllama(model="mistral")
#
#     # 3. Load local embedding model
#     embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#
#     # 4. Create FAISS vector store
#     vectorstore = FAISS.from_documents(chunks, embedding_model)
#
#     # 5. Build retriever
#     retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
#
#     # 6. Build RAG chain
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         return_source_documents=True
#     )
#
#     # 7. Ask the question
#     result = qa_chain({"query": question})
#
#     return result["result"]

