from fastapi import APIRouter, UploadFile, File
from typing import Annotated
from backend.services.documnet_loader import load_document
import uuid

router=APIRouter(
    prefix="/documents",
    tags=["Documnets"]
)

@router.post("/")
async def upload_files(
    file: Annotated[UploadFile, File(...)]
):
    content = await file.read()

    document_id = str(uuid.uuid4())

    load_document(content,document_id)  