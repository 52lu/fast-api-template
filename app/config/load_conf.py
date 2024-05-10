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
    envFile = os.environ.get("APP_ENV_FILE", "")
    if envFile != "":
        return envFile

    # 根据运行环境匹配配置文件
    return matchEnvFile()


def matchEnvFile() -> str:
    """ 根据运行环境匹配配置文件 """
    # 读取运行环境
    runEnv = os.environ.get("APP_ENV", "")
    # 默认加载.env
    _envFile = ".env"
    # 运行环境不为空加载 .env 文件
    if runEnv != "":
        # 当是其他环境时，如测试环境: 加载 .env.test 正式环境: 加载.env.prod
        _envFile = f".env.{runEnv}"

    # 默认查找当前目录和上级目录
    matchPath = ["", "../"]
    currentDir = os.getcwd()
    envFilePath = ""
    for path in matchPath:
        envFilePath = os.path.join(currentDir, path, _envFile)
        if os.path.exists(envFilePath):
            break

    return envFilePath


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
    # 使用 argparse 定义命令行参数
    parser = argparse.ArgumentParser(description="命令行参数")
    parser.add_argument("--env", type=str, default="", help="运行环境")
    parser.add_argument("--envfile", type=str, default="", help="直接指定配置文件")
    # 解析命令行参数
    args = parser.parse_args()
    # 设置环境变量
    os.environ["APP_ENV"] = args.env
    os.environ["APP_ENV_FILE"] = args.envfile


# 创建全局配置实例
globalAppSettings = getAppConfig()
