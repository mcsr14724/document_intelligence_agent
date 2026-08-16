import fitz

def extract_pdf_text(content: bytes):
    document = fitz.open(stream=content, filetype="pdf")

    pages = []

    for page_number, page in enumerate(document, start=1):
        pages.append({
            "page": page_number,
            "text": page.get_text()
        })

    document.close()

    return pages