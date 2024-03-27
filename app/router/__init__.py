#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:44 
"""

from app.router import (
    default_router,
    demo_router,
    di_router,
    param_router
)

# 定义路由列表
RegisterRouterList = [
    default_router,
    demo_router,
    di_router,
    param_router
]
