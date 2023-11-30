#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：main.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:44 
"""
import argparse

import uvicorn
from fastapi import FastAPI
from app.router import RegisterRouterList

# 实例化
app = FastAPI(redoc_url=None, docs_url="/apidoc", title="FastAPI模板")
# 加载路由
for item in RegisterRouterList:
    app.include_router(item.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
