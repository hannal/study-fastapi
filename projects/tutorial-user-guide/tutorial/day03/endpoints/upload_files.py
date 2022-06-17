from fastapi import File, UploadFile, status

from ..app import app


@app.post(
    "/files/",
    name="create_file",
    tags=["upload_files"],
    status_code=status.HTTP_201_CREATED,
)
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post(
    "/uploadfile/",
    name="create_upload_file",
    tags=["upload_files"],
    status_code=status.HTTP_201_CREATED,
)
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
