#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：http_error.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/7 7:49 PM
"""
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from app import utils


async def httpExceptionHandler(request, exc: HTTPException) -> JSONResponse:
    """自定义处理HTTPException"""
    print("request:", request)
    print("status_code:", exc.status_code)
    if exc.status_code == status.HTTP_404_NOT_FOUND:
        # 处理404错误
        return JSONResponse(
            content=jsonable_encoder(utils.ResponseFail("接口路由不存在~")),
            status_code=status.HTTP_200_OK,
        )
    elif exc.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
        # 处理405错误
        return JSONResponse(
            content=jsonable_encoder(utils.ResponseFail("请求方式错误，请查看文档确认~")),
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content=jsonable_encoder(utils.ResponseFail(str(exc))),
            status_code=status.HTTP_200_OK,
        )
