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
# from app.parameter.demo_param import DemoParam
# from app.parameter import DemoParam
from app import parameter

router = APIRouter(
    prefix="/demo",
    tags=["演示接口"]
)


@router.post("/query/pydantic/multiParamReceive")
async def multipleParamReceive(body: parameter.PydanticVerifyParam, order_id: int):
    """
    请求体和查询参数结合使用-演示
    """
    return {
        "msg": "请求体和查询参数结合使用",
        "result": {
            "body": body,
            "order_id": order_id,
        }
    }


@router.post("/query/pydantic/verify")
async def bodyReceive(body: parameter.PydanticVerifyParam):
    """
    pydantic模型验证-演示
    """
    return {
        "msg": "pydantic模型验证",
        "result": {
            "body": body,
        }
    }


@router.post("/query/body/receive")
async def bodyReceive(body: parameter.DemoParam):
    """
    请求体参数接受-演示
    """
    return {
        "msg": "请求体参数接受",
        "result": {
            "body": body,
        }
    }


@router.get("/query/receive")
async def queryParamReceive(username: str, sex: str = '男', city: Union[str, None] = "None"):
    """
    查询参数接受-演示
    """
    return {
        "msg": "查询参数接收",
        "result": {
            "username": username,
            "sex": sex,
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
