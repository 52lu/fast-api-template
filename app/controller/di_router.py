#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：di_router.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/25 22:01
"""
from fastapi import APIRouter, Depends
from app import depends, dao

router = APIRouter(prefix="/di", tags=["依赖项学习"], dependencies=[Depends(depends.verifyToken)])
# router = APIRouter(prefix="/di", tags=["依赖项学习"])


@router.get("/test")
async def test(user_id: int):
    """
    依懒项学习验证测试
    """
    return {"user_id": user_id}

