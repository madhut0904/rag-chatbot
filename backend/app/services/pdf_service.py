import fitz


def extract_pdf_pages(file_path: str):
    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text")

        pages.append({
            "page_number": page_number,
            "text": text.strip()
        })

    document.close()

    return pages