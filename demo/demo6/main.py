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


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


# from fastapi import FastAPI
#
# app = FastAPI()
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
