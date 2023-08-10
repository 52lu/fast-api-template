#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：indexController.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 11:45 
"""
from fastapi import APIRouter

from app.config import appSettings

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World", "conf": appSettings}
