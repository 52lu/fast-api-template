#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：admin.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:46 
"""
from app.utils import StringUtil


def DoLogin(userName: str, password: str) -> dict:
    """
    执行登录逻辑
    :param userName:
    :param password:
    :return:
    """
    return {
        "token": StringUtil.GenerateMd5(userName + password)
    }
