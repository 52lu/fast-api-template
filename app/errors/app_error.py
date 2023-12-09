#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：app_error.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/8 10:29 PM
"""

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.types import response


async def appExceptionHandler(request: Request, exc: Exception):
    """自定义全局系统错误"""
    return JSONResponse(
        content=jsonable_encoder(response.ResponseFail("系统运行异常,稍后重试~")),
        status_code=status.HTTP_200_OK,
    )
