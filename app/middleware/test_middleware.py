#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：usetime_middleware.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/12 7:25 PM
"""

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class TestMiddleware(BaseHTTPMiddleware):
    """ 测试顺序中间件"""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        print("调用-中间件-TestMiddleware---before")
        # 调用下一个中间件或路由处理函数
        result = await call_next(request)
        print("调用-中间件-TestMiddleware---after")
        return result
