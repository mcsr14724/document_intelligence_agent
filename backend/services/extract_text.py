import fitz


def extract_pdf_text(content: bytes):
    document = fitz.open(stream=content, filetype="pdf")

    pages = []
    current_position = 0

    for page_number, page in enumerate(document, start=1):

        text = page.get_text()

        start_position = current_position
        end_position = start_position + len(text)

        pages.append({
            "page": page_number,
            "text": text,
        })

        current_position = end_position

    document.close()

    return pages