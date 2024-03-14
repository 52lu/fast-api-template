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
from starlette.staticfiles import StaticFiles

from app import errors, middleware
from app.config import appSettings
from app.router import RegisterRouterList

# 实例化
server = FastAPI(redoc_url=None, docs_url="/apidoc", title="FastAPI学习")

# 挂载静态资源目录
server.mount("/static", StaticFiles(directory="static"), name="static")

# 注册自定义错误处理器
errors.registerCustomErrorHandle(server)
# 注册中间件
middleware.registerMiddlewareHandle(server)
# 加载路由
for item in RegisterRouterList:
    server.include_router(item.router)

print("appSettings:", appSettings)

if __name__ == "__main__":
    # 使用 python main.py 启动服务
    uvicorn.run(server, host=appSettings.app_host, port=appSettings.app_port)
