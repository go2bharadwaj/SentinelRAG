import os
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOllama
from langchain.chains import RetrievalQA

load_dotenv()


# Our main function: takes a document and a question, returns an answer
def process_query(text: str, question: str) -> str:
    # 1. Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    chunks = splitter.create_documents([text])

    # 2. Load local LLM
    llm = ChatOllama(model="mistral")

    # 3. Load local embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Create FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embedding_model)

    # 5. Build retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    # 6. Build RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    # 7. Ask the question
    result = qa_chain({"query": question})

    return result["result"]

