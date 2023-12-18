#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：app_config.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/15 4:41 PM
"""
from pydantic import BaseSettings, RedisDsn

class AppConfigSettings(BaseSettings):
    """应用配置"""
    app_name: str = 'FastAPI学习'
    app_port: int = 8080
    app_env: str = "dev"
    app_debug: bool = False
    """jwt配置"""
    jwt_secret_key: str = "12345789@98765431"
    jwt_algorithm: str = "HS256"
    jwt_expired: int = 30
    jwt_iss: str = "猿码记"
    jwt_no_check_uris: str = ""

    """数据库配置"""
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str
    """redis配置"""
    redis_dsn: RedisDsn = None
