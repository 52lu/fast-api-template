#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-fast-chat
@File    ：log.py
@Author  ：Mr.LiuQHui
@Date    ：2025/4/27 17:42
"""
from functools import lru_cache

from loguru import logger as _logger

from app.config import globalAppSettings
from .context import getTraceId


@lru_cache
def initLog() -> _logger:
    # 清除默认的 handler
    _logger.remove()
    _logger.add(
        globalAppSettings.log_file,  # 输出目的地（文件名、sys.stdout、函数、其他对象）
        level=globalAppSettings.log_level,  # 最低输出等级
        format=globalAppSettings.log_format,  # 日志格式
        colorize=True,  # 是否彩色输出
        serialize=globalAppSettings.log_serialize,  # 是否序列化成 JSON
        rotation=globalAppSettings.log_rotation,  # 日志轮转（按大小、时间、函数）
        retention=globalAppSettings.log_retention,  # 日志保留时间（过期自动删）
        compression=globalAppSettings.log_compression,  # 日志压缩（zip, tar, gz 等）
    )
    return _logger


_logger = initLog()


def getLogger() -> _logger:
    traceId = getTraceId()
    # 绑定 trace_id，得到一个新的 logger
    return _logger.bind(trace_id=traceId)


logger = getLogger()
