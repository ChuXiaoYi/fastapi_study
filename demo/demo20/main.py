# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2020/8/28 2:26 下午
#       @Author  : cxy =.=
#       @File    : main.py
#       @Software: PyCharm
#       @Desc    :
# ---------------------------------------------
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.file.read()
    return {"filename": file.filename}
