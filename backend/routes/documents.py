from fastapi import APIRouter, UploadFile, File
from typing import Annotated

router=APIRouter(
    prefix="/documents",
    tags=["Documnets"]
)

@router.post("/")
async def upload_files(
    files: Annotated[UploadFile,File(...)]
):
    pass