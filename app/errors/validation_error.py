#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：validation_error.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/6 8:02 PM
"""
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app import utils
from app import config
from fastapi.encoders import jsonable_encoder


async def validationExceptionHandler(request: Request, exc: RequestValidationError):
    """自定义参数验证异常错误"""
    errMsg = ""
    for error in exc.errors():
        fieldName = ".".join(error.get("loc"))
        errType = error.get("type")
        if errType in config.validateChineseDict:
            # 在定义错误模版中，并翻译出内容
            translateMsg = translate(fieldName, errType, error.get("ctx")) + "; "
            if translateMsg:
                errMsg += translateMsg
        else:
            # 不在定义模型，显示原始错误
            errMsg += (
                ".".join(error.get("loc"))
                + "["
                + error.get("type")
                + "]:"
                + error.get("msg")
                + "; "
            )

    # 替换body.
    errMsg = errMsg.replace("body.", "")
    # 返回
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(utils.ResponseFail(errMsg)),
    )


def translate(fieldName: str, errType: str, limitDict: dict) -> str:
    """翻译错误信息"""
    # 先判断是否满足关键词错误
    for k, v in config.keyErrorChineseDict.items():
        if fieldName.find(k) != -1:
            return v

    limitValList = limitDict.values()
    try:
        return config.validateChineseDict.get(errType).format(fieldName, *limitValList)
    except Exception as e:
        return ""
