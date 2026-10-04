
import os
import uuid

from app.services.pdf_service import extract_pdf_pages
from app.services.chunking_service import create_chunks
from app.services.embedding_service import create_embedding
from app.services.vector_service import client
from app.core.config import QDRANT_COLLECTION


PDF_PATH = "uploads/DBMS_RAG_Test_Notes.pdf"

DOCUMENT_ID = str(uuid.uuid4())
FILENAME = os.path.basename(PDF_PATH)

SUBJECT_ID = "dbms"


def index_pdf():

    print("=" * 60)
    print("PDF INDEXING STARTED")
    print("=" * 60)

    # --------------------------------------------------
    # 1. Check PDF
    # --------------------------------------------------

    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(
            f"PDF not found: {PDF_PATH}"
        )

    print(f"\nPDF: {FILENAME}")
    print(f"Document ID: {DOCUMENT_ID}")

    # --------------------------------------------------
    # 2. Extract PDF text
    # --------------------------------------------------

    print("\n[1/4] Extracting PDF text...")

    pages = extract_pdf_pages(PDF_PATH)

    print(f"Pages extracted: {len(pages)}")

    if not pages:
        raise ValueError("No pages found in PDF.")

    # --------------------------------------------------
    # 3. Create chunks
    # --------------------------------------------------

    print("\n[2/4] Creating chunks...")

    chunks = create_chunks(pages)

    print(f"Chunks created: {len(chunks)}")

    if not chunks:
        raise ValueError(
            "No text chunks were created. "
            "The PDF may contain scanned images instead of text."
        )

    # --------------------------------------------------
    # 4. Generate embeddings and upload to Qdrant
    # --------------------------------------------------

    print("\n[3/4] Creating embeddings and uploading to Qdrant...")

    points = []

    for index, chunk in enumerate(chunks):

        print(
            f"Processing chunk {index + 1}/{len(chunks)}..."
        )

        vector = create_embedding(
            chunk["text"]
        )

        payload = {
            "document_id": DOCUMENT_ID,
            "filename": FILENAME,
            "subject_id": SUBJECT_ID,
            "page_number": chunk["page_number"],
            "chunk_index": chunk["chunk_index"],
            "text": chunk["text"],
        }

        points.append(
            {
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": payload,
            }
        )

    # --------------------------------------------------
    # 5. Upload points to Qdrant
    # --------------------------------------------------

    print("\n[4/4] Uploading vectors to Qdrant...")

    client.upsert(
        collection_name=QDRANT_COLLECTION,
        points=points,
        wait=True
    )

    print("\n" + "=" * 60)
    print("PDF INDEXING COMPLETED")
    print("=" * 60)

    print(f"Collection: {QDRANT_COLLECTION}")
    print(f"Document: {FILENAME}")
    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Uploaded points: {len(points)}")


if __name__ == "__main__":
    index_pdf()