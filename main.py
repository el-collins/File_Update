from typing import Annotated, List

from fastapi import FastAPI, File, UploadFile

app = FastAPI()



@app.post("/files/")
async def check_size(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(files: List[UploadFile]):
    result = []

    for file in files:
        result.append(file.filename.split(".")[-1])
    return {"The file extensions": result}
