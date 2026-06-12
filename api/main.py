from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
import uuid

app = FastAPI(title="ResearchMate API", version="0.1.0")
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF uploads are accepted.")
    dest = UPLOAD_DIR / f"{uuid.uuid4()}.pdf"
    content = await file.read()
    with dest.open("wb") as f:
        f.write(content)
    # Placeholder: enqueue processing job, extract text, etc.
    return {"filename": file.filename, "stored_as": str(dest)}

@app.get("/summary/{paper_id}")
async def summary(paper_id: str):
    # Placeholder for LLM summarization result lookup
    return {"paper_id": paper_id, "summary": "Summary not implemented yet."}
