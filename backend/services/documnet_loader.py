from backend.services.extract_text import extract_pdf_text
from backend.services.chunking import chunker
from backend.services.ingestion import ingest


def load_document(content,document_id):
    pages = extract_pdf_text(content)

    chunks = chunker(pages)

    ingest(chunks,document_id)