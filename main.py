#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：main.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 11:11 
"""
import uvicorn
from app.bootstrap import *

if __name__ == '__main__':
    uvicorn.run(appServer, port=appSettings.service_port)