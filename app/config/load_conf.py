#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：load_conf.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/22 12:22
"""
import os
from functools import lru_cache
import argparse

from dotenv import load_dotenv
from app import config


def getEnvFile() -> str:
    """ 获取加载的配置文件"""
    # 读取运行环境
    runEnv = os.environ.get("APP_ENV", "")
    # 默认加载.env
    envFile = ".env"
    # 运行环境不为空加载 .env 文件
    if runEnv != "":
        # 当是其他环境时，如测试环境: 加载 .env.test 正式环境: 加载.env.prod
        envFile = f".env.{runEnv}"
    return envFile


@lru_cache
def getAppConfig() -> config.AppConfigSettings:
    """ 获取项目配置 """
    # 解析命令行参数
    parseCliArgument()
    # 获取配置文件
    envFile = getEnvFile()
    print("获取配置文件: ", envFile)
    # 加载配置
    load_dotenv(envFile)
    # 实例化配置模型
    return config.AppConfigSettings()


def parseCliArgument():
    """ 解析命令行参数 """
    import sys
    # print("解析命令行参数:", sys.argv[0])
    # if "uvicorn" in sys.argv[0]:
    #     # TODO 使用uvicorn启动,则解析--env-file文件
    #     print("使用uvicorn启动....")
    #     return
    # 使用 argparse 定义命令行参数
    parser = argparse.ArgumentParser(description="命令行参数")
    parser.add_argument("--env", type=str, default="", help="运行环境")
    # 解析命令行参数
    args = parser.parse_args()
    # 设置环境变量
    # uvicorn模式启动，读取的.env*里面的APP_ENV
    os.environ["APP_ENV"] = args.env


# 创建全局配置实例
globalAppSettings = getAppConfig()
