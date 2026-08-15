from fastapi import APIRouter
from backend.schemas.chat import ChatRequest,ChatResponse

router=APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/",response_model=ChatResponse)
def chat(user_query:ChatRequest):
    pass