#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：open.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:45
"""
from typing import Union

from fastapi import APIRouter

router = APIRouter(
    prefix="/demo",
    tags=["演示接口"]
)


@router.get("/query/receive")
async def queryParamReceive(username: str, password: str, age: int = 18, city: Union[str, None] = None):
    """
    查询参数接受-演示
    """
    return {
        "msg": "查询参数接收",
        "result": {
            "username": username,
            "password": password,
            "age": age,
            "city": city,
        }
    }


@router.get("/path/test")
async def pathParamReceive2():
    """
    路径参数接收-演示-不带路径参数
    """
    return {
        "msg": "hello",
    }


@router.get("/path/{order_id}")
async def pathParamReceive(order_id: int):
    """
    路径参数接收-演示-带路径参数
    """
    return {
        "接受结果": order_id,
    }
