#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：user_proto.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/10 16:00
"""
from typing import Optional, Union

from pydantic import BaseModel, Field


class UserListRequest(BaseModel):
    """
    用户列表入参
    """

    nick_name: Optional[str] = Field(default="", description="用户昵称", examples=["张三"])
    phone: Union[str, None] = Field(None, description="填写手机号", examples=["17600000000"])
    page: Optional[int] = Field(default=1, description="页", examples=["1"])
    pageSize: Optional[int] = Field(default=10, description="每页数量", examples=["10"])


class UserDetailProto(BaseModel):
    """
    用户详情
    """
    id: int = Field(description="主键id")
    union_id: str = Field(description="微信开放平台下的用户唯一标识")
    open_id: str = Field(description="微信openid")
    nick_name: str = Field(description="昵称")
    avatar: str = Field(description="头像")
    phone: str = Field(description="手机号")
    email: str = Field(description="邮箱")
    last_login: str = Field(description="上次登录时间")
    status: int = Field(description="状态；-1:黑名单 1:正常")
    delete_at: str = Field(description="删除时间")
    created_at: str = Field(description="创建时间")
    updated_at: str = Field(description="更新时间")


class UserListResponse(BaseModel):
    """
    用户列表出参
    """

    record_total: int = Field(default=0, description="总量")
    record_list: list[UserDetailProto] = Field(default=[])
