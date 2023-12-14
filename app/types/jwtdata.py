#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：jwtdata.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/14 6:05 PM
"""
from pydantic import BaseModel, Field


class JwtData(BaseModel):
    """ jwt中业务数据 """
    uid: int = Field(default=0)  # 用户id
    uname: str = Field(default="")  # 用户姓名
