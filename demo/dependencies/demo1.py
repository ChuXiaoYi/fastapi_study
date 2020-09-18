# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2020/9/18 11:24 上午
#       @Author  : cxy =.=
#       @File    : demo1.py
#       @Software: PyCharm
#       @Desc    :
# ---------------------------------------------
from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
