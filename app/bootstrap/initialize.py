#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：initialize.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/9 16:08
"""
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app import errors, middleware
from app.router import RegisterRouterList


def Init(server: FastAPI):
    """ 初始化项目"""
    # 挂载静态资源目录
    server.mount("/static", StaticFiles(directory="static"), name="static")

    # 注册自定义错误处理器
    errors.registerCustomErrorHandle(server)
    # 注册中间件
    middleware.registerMiddlewareHandle(server)
    # 加载路由
    for item in RegisterRouterList:
        server.include_router(item.router)
