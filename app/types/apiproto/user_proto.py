#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：user_proto.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/10 16:00
"""
from typing import Optional

from pydantic import BaseModel, Field


class UserListRequest(BaseModel):
    """
    用户列表入参
    """

    nick_name: str = Field(default="", description="用户昵称", examples=["张三"])
    page: int = Field(default=1, description="页", examples=["1"])
    pageSize: int = Field(default=10, description="每页数量", examples=["10"])


class UserListResponse(BaseModel):
    """
    用户列表出参
    """

    record_total: int = Field(default="", description="")
