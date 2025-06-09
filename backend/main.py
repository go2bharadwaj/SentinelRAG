from fastapi import FastAPI, UploadFile, File
from rag_pipeline import process_query
import pdfplumber
import io

app = FastAPI()

def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@app.post("/ask")
async def ask_question(file: UploadFile = File(...), question: str = ""):
    contents = await file.read()

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(contents)
    else:
        text = contents.decode("utf-8", errors="ignore")  # fallback for text files

    answer = process_query(text, question)
    return {"answer": answer}

