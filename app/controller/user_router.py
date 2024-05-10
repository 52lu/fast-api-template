#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：user_router.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/10 15:00
"""
from fastapi import APIRouter

from app.types import apiproto

router = APIRouter(prefix="/user", tags=["用户相关接口"])


@router.post("/list")
async def userList(body: apiproto.UserListRequest):
    """
    用户列表-演示
    """

    return {
        "msg": "请求体参数接受",
        "result": {
            "body": body,
        },
    }
