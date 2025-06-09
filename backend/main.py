from fastapi import FastAPI, UploadFile, File, Form
from rag_pipeline import *
import pdfplumber
import io

app = FastAPI()

def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Upload endpoint (used once per doc)
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(contents)
    else:
        text = contents.decode("utf-8", errors="ignore")

    store_embeddings(text)
    return {"status": "Document uploaded and processed successfully."}

# Ask endpoint
@app.post("/ask")
async def ask_question(question: str = Form(...)):
    answer = query_index(question)
    return {"answer": answer}

@app.delete("/delete_vectorDB")
async def delete_vectordb():
    deleteVectorStore()
    return {"status": "Vector DB deleted successfully."}
