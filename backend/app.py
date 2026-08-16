from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.database.qdrantdb import create_collection
from backend.routes.documents import router as document_router
from backend.routes.chat import router as chat_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_collection()
    yield


app = FastAPI(
    title="Document Intelligence Agent",
    description="RAG-based document search and intelligence API",
    lifespan=lifespan
)

app.include_router(document_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Document Intelligence Agent is running"
    }