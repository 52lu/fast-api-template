#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：index_router.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 18:45 
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index():
    """
    默认访问链接
    """
    return {"message": "Hello World!"}
