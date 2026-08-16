from qdrant_client import QdrantClient, models
from backend.config import Config

qdrantdb_client=QdrantClient(
    api_key=Config.QDRANT_API_KEY,
    url=Config.QDRANT_URL,
    cloud_inference=True
)

def create_collection():
    if not qdrantdb_client.collection_exists(Config.QDRANT_COLLECTION):
        qdrantdb_client.create_collection(
            collection_name=Config.QDRANT_COLLECTION,
            vectors_config={
                "dense": models.VectorParams(
                    size=Config.EMBEDDING_SIZE,
                    distance=models.Distance.COSINE
                )
            },
            sparse_vectors_config={
                "sparse":models.SparseVectorParams(
                    modifier=models.Modifier.IDF
                )
            }
        )