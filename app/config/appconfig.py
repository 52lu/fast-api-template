#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：appconfig.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 12:28 
"""
from pydantic import BaseSettings


class AppConfig(BaseSettings):
    # 定义属性
    service_port: int = 8000
    service_host: str = "0.0.0.0"
    service_name: str = "AI学习演示"
    service_version: str = "v1.0.0"
    hugging_face_token: str = ""
    img_path: str = "./tmp"

    # 指定读取env
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

