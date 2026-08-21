from backend.services.embeddings import embedding_model, sparse_embedding_model
from langchain_qdrant import QdrantVectorStore, RetrievalMode
from langchain_core.documents import Document
from backend.config import Config
import time

def ingest(chunks,document_id):
    documents = []

    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk["chunk"],
                metadata={
                    "document_id":document_id,
                    "chunk_id": chunk["chunk_id"],
                    "page": chunk["page"],
                }
            )
        )

    BATCH_SIZE = 90

    for start in range(0, len(documents), BATCH_SIZE):

        batch = documents[start:start + BATCH_SIZE]

        QdrantVectorStore.from_documents(
            documents=batch,
            embedding=embedding_model,
            sparse_embedding=sparse_embedding_model,
            url=Config.QDRANT_URL,
            api_key=Config.QDRANT_API_KEY,
            collection_name=Config.QDRANT_COLLECTION,
            retrieval_mode=RetrievalMode.HYBRID,
            vector_name="dense",
            sparse_vector_name="sparse"
        )

        if start + BATCH_SIZE < len(documents):
            time.sleep(60)