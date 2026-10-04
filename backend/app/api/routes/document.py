from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid

from app.services.pdf_service import extract_pdf_pages
from app.services.chunking_service import create_chunks

router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    document_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{document_id}.pdf"
    )

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    pages = extract_pdf_pages(file_path)
    chunks = create_chunks(pages)

    return {
        "document_id": document_id,
        "filename": file.filename,
        "pages": len(pages),
        "chunks": len(chunks)
    }