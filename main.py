#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：main.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 17:44 
"""

import uvicorn
from fastapi import FastAPI

from app import bootstrap
from app.config import globalAppSettings

if __name__ == "__main__":
    print("打印项目配置:", globalAppSettings)
    # 实例化
    server = FastAPI(redoc_url=None, docs_url="/apidoc", title=globalAppSettings.app_name)
    # 初始化项目
    bootstrap.Init(server)
    # 使用 python main.py 启动服务
    uvicorn.run(server, host=globalAppSettings.app_host, port=globalAppSettings.app_port)
