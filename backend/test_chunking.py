from app.services.pdf_service import extract_pdf_pages
from app.services.chunking_service import create_chunks


PDF_PATH = "uploads/DBMS_RAG_Test_Notes.pdf"


def main():

    print("Reading PDF...")

    pages = extract_pdf_pages(PDF_PATH)

    print("Pages:", len(pages))

    chunks = create_chunks(pages)

    print("Chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:5], start=1):

        print("\n" + "=" * 60)
        print("Chunk:", i)
        print("Page:", chunk["page_number"])
        print("Chunk index:", chunk["chunk_index"])
        print("Characters:", len(chunk["text"]))
        print("Text:")
        print(chunk["text"][:500])


if __name__ == "__main__":
    main()