#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：usetime_middleware.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/12 7:25 PM
"""
import json
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from app.logcore import log
from app.config import globalAppSettings

from app.logcore import context


class RequestMiddleware(BaseHTTPMiddleware):
    """ 记录请求中间件"""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        # 设置traceId
        context.setTraceId()
        logger = log.getLogger()

        start_time = time.time()
        # 获取请求体（要先读取，再重建，否则会被消费掉）
        body = await request.body()
        noCheckTokenPathList = globalAppSettings.jwt_no_check_uris.split(",")
        if request.url.path in noCheckTokenPathList:
            return await call_next(request)

        body_data = body.decode("utf-8") if body else ""

        logBody = json.dumps({
            "url": request.url.path,
            "method": request.method,
            "header": dict(request.headers),
            "post_param": body_data,
            "query_param": dict(request.query_params),
        })
        logger.info(f"请求入口:{request.url.path} {logBody}")

        response = await call_next(request)
        # 记录响应内容（只限 JSON / 文本响应）
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        response_text = response_body.decode("utf-8", errors="ignore")
        try:
            response_json = json.loads(response_text)
        except Exception:
            response_json = response_text

        # 耗时
        useTime = time.time() - start_time
        logBody = json.dumps({
            "result": response_json,
            "use_time": useTime,
        })

        logger.info(f"响应返回:{request.url.path} {logBody}")
        resp = Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
        # tradeIdCtx.reset(tradeIdCtx)
        return resp
