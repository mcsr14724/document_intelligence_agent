from fastapi import APIRouter

router=APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
def chat(user_query:str):
    pass