#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：bootstrap.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 17:27 
"""

from fastapi import FastAPI
from app.config import appSettings
from app.controller import indexController

# 创建app
appServer = FastAPI(
    version=appSettings.service_version,
    title=appSettings.service_name
)

# 注册路由
appServer.include_router(indexController.router)
