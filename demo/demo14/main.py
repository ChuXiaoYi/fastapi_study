# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2020/8/28 2:26 下午
#       @Author  : cxy =.=
#       @File    : main.py
#       @Software: PyCharm
#       @Desc    :
# ---------------------------------------------
from typing import List, Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
        user_agent: Optional[str] = Header(None, convert_underscores=False),
        x_token: Optional[List[str]] = Header(None)
):
    return {"User-Agent": user_agent, "X-Token values": x_token}
