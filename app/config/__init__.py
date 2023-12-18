#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 18:24 
"""
from functools import lru_cache

from dotenv import load_dotenv

from .validate_template_config import validateChineseDict, keyErrorChineseDict
from .app_config import *


@lru_cache
def getAppConfig() -> AppConfigSettings:
    # 加载 .env 文件，dotenv_path 变量默认是.env
    load_dotenv()
    # 实例化配置模型
    return AppConfigSettings()


# 获取配置
appSettings = getAppConfig()
