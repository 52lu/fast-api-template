#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 18:24 
"""
import os
from functools import lru_cache
import argparse

from dotenv import load_dotenv

from .validate_template_config import validateChineseDict, keyErrorChineseDict
from .app_config import *


@lru_cache
def getAppConfig() -> AppConfigSettings:
    """ 获取项目配置 """
    # 解析命令行参数
    parseCliArgument()
    # 读取运行环境
    runEnv = os.environ.get("APP_ENV", "")
    print("运行环境: ", runEnv)
    # 默认加载.env
    envFile = ".env"
    # 运行环境不为空加载 .env 文件
    if runEnv != "":
        # 当是其他环境时，如测试环境: 加载 .env.test 正式环境: 加载.env.prod
        envFile = f".env.{runEnv}"
    # 加载配置
    load_dotenv(envFile)
    # 实例化配置模型
    return AppConfigSettings()


def parseCliArgument():
    """ 解析命令行参数 """
    import sys
    if "uvicorn" in sys.argv[0]:
        print(sys.argv[0])
        return
    # 使用 argparse 定义命令行参数
    parser = argparse.ArgumentParser(description="命令行参数")
    parser.add_argument("--env", type=str, default="", help="运行环境")
    # 解析命令行参数
    args = parser.parse_args()
    # 设置环境变量
    # uvicorn模式启动，读取的.env*里面的APP_ENV
    os.environ["APP_ENV"] = args.env


# 创建配置实例
globalAppSettings = getAppConfig()
