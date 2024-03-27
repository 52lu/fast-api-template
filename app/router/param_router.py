#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：cookie_router.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/27 22:29
"""
from typing import Annotated

from fastapi import APIRouter, Cookie, Request

router = APIRouter(prefix="/param", tags=["更多参数接收示例"])


@router.get("/cookie/key", summary="接收cookie中指定的key")
async def cookieKey(user_name: Annotated[str | None, Cookie()] = None):
    """接收cookie中指定的key"""
    return {"user_name": user_name}


@router.get("/cookie/all", summary="所有cookie值")
async def cookieParams(request: Request):
    """接收cookie值"""
    return {"cookies": request.cookies}
