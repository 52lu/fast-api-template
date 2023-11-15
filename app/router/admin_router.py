#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：user.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:44 
"""
from typing import Union

from fastapi import APIRouter
from app.service import admin_service

router = APIRouter(
    prefix="/admin",
    tags=["后台相关接口","admin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "admin下,路由不存在~"}},
)


# 中间件
@router.get("/index")
async def index():
    """
    后台首页
    """
    return {
        "code": 0,
        "message": "请登录~"
    }


@router.get("/login")
async def login(userName: str | None = '', password: str | None = ''):
    """
    后台登录接口
    """
    if userName == "" or password == "":
        return {"code": 0, "message": "用户名和密码不能为空~"}

    return admin_service.DoLogin(userName, password)
