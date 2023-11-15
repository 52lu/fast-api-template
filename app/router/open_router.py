#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：open.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:45
"""
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(
    prefix="/open",
    tags=["open"]
)


@router.get('/config')
async def config():
    """
    配置信息
    """
    return {
        "code": 200,
        "message": {
            "app_name": "FastAPI框架学习",
            "app_version": "v0.0.1",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }
