from fastapi import FastAPI


app = FastAPI(
    title="Document Intelligence Agent",
    description="RAG-based document search and intelligence API",
)


@app.get("/")
def root():
    return {
        "message": "Document Intelligence Agent is running"
    }