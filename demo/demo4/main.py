# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/9/26 3:22 PM
#       @Author  : cxy =.= 
#       @File    : main.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path}

