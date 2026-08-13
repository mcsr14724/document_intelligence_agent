from qdrant_client import QdrantClient
from backend.config import Config

qdrantdb_client=QdrantClient(
    api_key=Config.QDRANT_API_KEY,
    url=Config.QDRANT_URL
)