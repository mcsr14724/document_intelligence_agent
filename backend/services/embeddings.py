from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse
from backend.config import Config

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    api_key=Config.GEMINI_API_KEY
)

sparse_embedding_model = FastEmbedSparse(
    model_name="Qdrant/bm25"
)