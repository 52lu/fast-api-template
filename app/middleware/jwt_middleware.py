#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：jwt_middleware.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/14 6:58 PM
"""

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.types import JwtData
from app.utils import JwtManageUtil
from app import utils
from app.config import globalAppSettings


# 后期做配置，这里临时演示
# secret_key = "abcd12345@abcdef"

# 不检查
# noCheckTokenPathList = [
#     "/apidoc",
#     "/openapi.json",
#     "/api/user/login"
# ]


class JwtMiddleware(BaseHTTPMiddleware):
    """jwt验证中间件"""

    def __init__(self, app):
        super().__init__(app)
        self.jwtUtil = JwtManageUtil(
            secretKey=globalAppSettings.jwt_secret_key,
            algorithm=globalAppSettings.jwt_algorithm,
            expired=globalAppSettings.jwt_expired,
            iss=globalAppSettings.jwt_iss,
        )

    async def dispatch(self, request: Request, call_next):
        # 判断路由是否需要验证
        path = request.url.path
        # 不检查的路由
        noCheckTokenPathList = globalAppSettings.jwt_no_check_uris.split(",")
        print("不检查的路由:", noCheckTokenPathList)
        if path in noCheckTokenPathList:
            return await call_next(request)
        # 获取token
        token = request.headers.get("x-token", "")
        if token == "":
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(utils.ResponseFail("token不能为空~")),
            )

        # 验证token
        tokenInfo = self.jwtUtil.decode(token, JwtData)
        if not isinstance(tokenInfo, JwtData):
            # 验证失败
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(utils.ResponseFail(tokenInfo)),
            )

        result = await call_next(request)
        print("token解析成功", tokenInfo)
        return result
