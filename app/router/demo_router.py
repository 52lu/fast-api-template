#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：open.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:45
"""
import time
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(
    prefix="/demo",
    tags=["演示接口"]
)


@router.get('/config')
async def config():
    begin = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    """
    配置信息
    """
    time.sleep(5)
    return {
        "code": 200,
        "message": {
            "app_name": "FastAPI框架学习",
            "app_version": "v0.0.1",
            "begin_time": begin,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }


@router.get("/path/{order_id}")
async def pathParamReceive(order_id: int):
    """
    路径参数接收演示
    """
    return {
        "接受结果": order_id,
    }
