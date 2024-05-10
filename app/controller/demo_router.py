#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：open.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:45
"""
import json
import random
import time
from typing import Union, Annotated

from fastapi import APIRouter, Header, Cookie
from fastapi.encoders import jsonable_encoder

from app.types import apiproto
from app import utils
from app.utils import logger

router = APIRouter(prefix="/demo", tags=["演示接口"])


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


@router.get("/query/receive")
async def queryParamReceive(
    username: str, sex: str = "男", city: Union[str, None] = "None"
):
    """
    查询参数接受-演示
    """
    return {
        "msg": "查询参数接收",
        "result": {
            "username": username,
            "sex": sex,
            "city": city,
        },
    }


@router.post("/query/body/receive")
async def bodyReceive(body: apiproto.DemoParam):
    """
    请求体参数接受-演示
    """
    return {
        "msg": "请求体参数接受",
        "result": {
            "body": body,
        },
    }


@router.post("/query/pydantic/verify")
async def bodyReceive(body: apiproto.PydanticVerifyParam):
    """
    pydantic模型验证-演示
    """
    return {
        "msg": "pydantic模型验证",
        "result": {
            "body": body,
        },
    }


@router.post("/query/pydantic/paramMixReceive")
async def multipleParamReceive(body: apiproto.PydanticVerifyParam, order_id: int):
    """
    请求体和查询参数混合使用-演示
    """
    return {
        "msg": "请求体和查询参数结合使用",
        "result": {
            "body": body,
            "order_id": order_id,
        },
    }


@router.post("/query/pydantic/multipleParamReceive")
async def multipleParamReceive(
    student: apiproto.StudentParam, classInfo: apiproto.ClassInfoParam
):
    """
    请求体-多参数接收-演示
    """
    #  orjson.dumps(stu).decode("utf-8")
    # logger.info("multipleParamReceive入参信息:%s",
    #             orjson.dumps({"student": student, "classInfo": classInfo}).decode("utf-8"))
    logger.info(
        "multipleParamReceive入参信息:%s",
        json.dumps(
            {
                "student": jsonable_encoder(student),
                "classInfo": jsonable_encoder(classInfo),
            }
        ),
    )

    return {
        "msg": "请求体-多参数接收",
        "result": {
            "student": student,
            "classInfo": classInfo,
        },
    }


@router.post("/query/pydantic/nestedModel")
async def nestedModelDemo(param: apiproto.NestedParam):
    """
    请求体-嵌套模型接收-演示
    """
    return {
        "msg": "嵌套模型接收使用-示例",
        "result": {
            "param": param,
        },
    }


@router.post("/query/pydantic/fieldDemo", summary="字段field演示")
async def fieldDemo(param: apiproto.FieldParam):
    """
    请求体-字段field-演示
    """
    return {
        "msg": "嵌套模型接收使用-示例",
        "result": {
            "param": param,
        },
    }


@router.post("/resp/demo", summary="响应模型示例", response_model_exclude_unset=True)
async def respDemo(param: apiproto.FieldParam) -> utils.HttpResponse:
    """
    响应模型示例-演示
    """
    if "游戏" in param.likes:
        return utils.ResponseFail("禁止玩游戏~")

    return utils.ResponseSuccess(param)


@router.get("/error/demo")
async def errorDemo() -> utils.HttpResponse:
    """
    异常示例-演示
    """
    result = "name{} age{}".format("张三")

    return utils.ResponseSuccess(result)


@router.get("/middle/useTime")
async def middleUseTime() -> utils.HttpResponse:
    """
    中间件使用-演示
    """
    seconds = random.randint(500, 5000) / 1000
    print("暂停时间:", seconds)
    time.sleep(seconds)
    return utils.ResponseSuccess(seconds)


# @router.get("/header/param")
# async def headParam(x_token: Annotated[list[str] | None, Header()] = None):
#     return {"X-Token values": x_token}
