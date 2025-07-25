#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-fast-chat
@File    ：context.py
@Author  ：Mr.LiuQHui
@Date    ：2025/4/27 18:02
"""

import contextvars
import socket

from app.utils import StringUtil

trace_id_ctx_var = contextvars.ContextVar("trace_id", default="-")


def setTraceId():
    tradeId = StringUtil.getTraceId()
    hostName = socket.gethostname()
    trace_id_ctx_var.set(f"{hostName}_{tradeId}")
    return trace_id_ctx_var


def getTraceId() -> str:
    return trace_id_ctx_var.get()
