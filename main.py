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

from app import initialize
from app.config import globalAppSettings
from app.router import RegisterRouterList

# 实例化
server = FastAPI(redoc_url=None, docs_url="/apidoc", title="FastAPI学习")
# 初始化项目
initialize.Init(server)


# # 挂载静态资源目录
# server.mount("/static", StaticFiles(directory="static"), name="static")
#
# # 注册自定义错误处理器
# errors.registerCustomErrorHandle(server)
# # 注册中间件
# middleware.registerMiddlewareHandle(server)
# # 加载路由
# for item in RegisterRouterList:
#     server.include_router(item.router)

# print("globalAppSettings:", globalAppSettings)

if __name__ == "__main__":
    # 使用 python main.py 启动服务
    uvicorn.run(server, host=globalAppSettings.app_host, port=globalAppSettings.app_port)
