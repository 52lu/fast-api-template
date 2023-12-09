#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/6 7:53 PM
"""
from fastapi import FastAPI

from .validation_error import validationExceptionHandler
from .http_error import httpExceptionHandler
from .app_error import appExceptionHandler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


def registerCustomErrorHandle(server: FastAPI):
    """ 统一注册自定义错误处理器 """
    # 注册参数验证错误,并覆盖模式RequestValidationError
    server.add_exception_handler(RequestValidationError, validationExceptionHandler)
    # 错误处理StarletteHTTPException
    server.add_exception_handler(StarletteHTTPException, httpExceptionHandler)
    # 自定义全局系统错误
    server.add_exception_handler(Exception, appExceptionHandler)
