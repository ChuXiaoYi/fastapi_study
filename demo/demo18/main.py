# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2020/8/28 2:26 下午
#       @Author  : cxy =.=
#       @File    : main.py
#       @Software: PyCharm
#       @Desc    :
# ---------------------------------------------
from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
