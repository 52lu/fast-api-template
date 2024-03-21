#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/19 22:45
"""

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.staticfiles import StaticFiles

from app import errors, middleware
from app.config import globalAppSettings
from app.router import RegisterRouterList

# 创建数据库连接
engine = create_engine(
    globalAppSettings.db_dsn,
    encoding='utf-8',  # 编码
    echo=globalAppSettings.db_echo_sql,  # 是否打印SQL
    pool_size=globalAppSettings.db_pool_size,  # 连接池的大小，指定同时在连接池中保持的数据库连接数，默认:5
    max_overflow=globalAppSettings.db_max_overflow,  # 超出连接池大小的连接数，超过这个数量的连接将被丢弃,默认: 5
)

# 创建会话工厂
GlobalSessionLocal = sessionmaker(bind=engine)


def Init(server: FastAPI):
    """ 初始化项目"""
    # 挂载静态资源目录
    server.mount("/static", StaticFiles(directory="static"), name="static")

    # 注册自定义错误处理器
    errors.registerCustomErrorHandle(server)
    # 注册中间件
    middleware.registerMiddlewareHandle(server)
    # 加载路由
    for item in RegisterRouterList:
        server.include_router(item.router)

    print("globalAppSettings:", globalAppSettings)
