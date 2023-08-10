#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：httputil.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 17:35 
"""
import datetime
import time


class HttpResponse:
    __code: int = 200
    __msg: str = "success"
    __data: None

    def __init__(self, code: int, msg: str, data: None):
        self.__code = code
        self.__msg = msg
        self.__data = data


def HttpSuccess(data):
    return {
        "code": 200,
        "msg": "success",
        "data": data,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def HttpFail(msg: str):
    return {
        "code": -1,
        "msg": msg,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
