# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2020/8/28 2:26 下午
#       @Author  : cxy =.=
#       @File    : main.py
#       @Software: PyCharm
#       @Desc    :
# ---------------------------------------------
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
