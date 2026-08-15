from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    thread_id: Optional[str] = None
    user_query: str

class ChatResponse(BaseModel):
    thread_id: str
    response: str