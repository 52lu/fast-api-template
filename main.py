#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：main.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:44 
"""

import uvicorn
from fastapi import FastAPI

from app import errors, middleware
from app.router import RegisterRouterList

# 实例化
server = FastAPI(redoc_url=None, docs_url="/apidoc", title="FastAPI学习")

# 注册自定义错误处理器
errors.registerCustomErrorHandle(server)
# # 注册中间件
middleware.registerMiddlewareHandle(server)

# 加载路由
for item in RegisterRouterList:
    server.include_router(item.router)

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=8000)
