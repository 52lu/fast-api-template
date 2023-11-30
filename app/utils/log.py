#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template 
@File    ：log.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/20 22:21 
"""

import logging

# 创建Logger对象
import os

logger = logging.getLogger(__name__)
# 设置标准日志等级
logger.setLevel(logging.DEBUG)

# 如果不存在定义的日志目录就创建一个
logfile_dir = "./logs"
logfile_name = "app.log"
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# 创建FileHandler对象，将日志写入文件
logfile_path = os.path.join(logfile_dir, logfile_name)
file_handler = logging.FileHandler(logfile_path, mode='w')
# 设置文件中写入的日志等级
file_handler.setLevel(logging.DEBUG)

# 创建StreamHandler对象，将日志输出到控制台
stream_handler = logging.StreamHandler()
# 设置控制台显示的日志等级
stream_handler.setLevel(logging.DEBUG)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将处理器添加到Logger对象中（注册）
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
