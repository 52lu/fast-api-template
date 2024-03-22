#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：app_config.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/15 4:41 PM
"""
from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class AppConfigSettings(BaseSettings):
    """应用配置"""

    """基础配置"""
    app_name: str = "FastAPI学习"
    app_host: str = "0.0.0.0"
    app_port: int = 8080
    app_env: str = "dev"
    app_debug: bool = False
    """jwt配置"""
    jwt_enable: bool = True
    jwt_secret_key: str = "12345789@98765431"
    jwt_algorithm: str = "HS256"
    jwt_expired: int = 30
    jwt_iss: str = "猿码记"
    jwt_no_check_uris: str = ""
    """数据库配置"""
    db_dsn: str = ""  # mysql+pymysql://username:password@localhost:3306/database_name
    db_echo_sql: bool = False  # 使用打印SQL日志信息
    db_pool_size: int = 5  # 连接池中的初始连接数，默认为 5
    db_max_overflow: int = 10  # 连接池中允许的最大超出连接数
    """redis配置"""
    redis_dsn: RedisDsn = None
