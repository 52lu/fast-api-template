#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：index_router.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 18:45 
"""
from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index():
    """
    默认访问链接
    """
    return {
        "code": 200,
        "msg": "Hello World!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
