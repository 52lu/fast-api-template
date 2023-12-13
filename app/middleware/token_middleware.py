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


class TokenMiddleware(BaseHTTPMiddleware):
    """ token验证中间件 """

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        token = request.headers.get("X-Token", "")
        print("调用-token验证中间件-TokenMiddleware---before", token)
        result = await call_next(request)
        print("调用-token验证中间件-TokenMiddleware---after", token)
        return result
