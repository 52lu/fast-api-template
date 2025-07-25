#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 18:25 
"""
from fastapi import FastAPI

# from .test_middleware import TestMiddleware
from .token_middleware import TokenMiddleware
from .usetime_middleware import UseTimeMiddleware
from .jwt_middleware import JwtMiddleware
from .request_middleware import RequestMiddleware
from app.config import globalAppSettings

# 定义注册顺序
middlewareList = [
    RequestMiddleware,  # 请求记录
    JwtMiddleware,  # jwt
    # UseTimeMiddleware,  # 添加耗时请求中间件
    TokenMiddleware,  # 添加token验证中间件
]


def registerMiddlewareHandle(server: FastAPI):
    """ 注册中间件 """

    # jwt未开启则不注册
    if globalAppSettings.jwt_enable is False:
        middlewareList.remove(JwtMiddleware)

    # 倒序中间件
    middlewareList.reverse()
    # 遍历注册
    for _middleware in middlewareList:
        server.add_middleware(_middleware)
