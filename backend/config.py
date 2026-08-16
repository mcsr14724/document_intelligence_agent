from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    QDRANT_API_KEY=os.getenv("QDRANT_API_KEY")
    QDRANT_URL=os.getenv("QDRANT_URL")
    QDRANT_COLLECTION=os.getenv("QDRANT_COLLECTION")
    EMBEDDING_SIZE=os.getenv("EMBEDDING_SIZE")