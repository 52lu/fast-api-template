#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：tokenVerify.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/25 22:08
"""

from fastapi import Header, HTTPException


async def verifyToken(x_token: str = Header()):
    """ token验证 """
    print("x_token:", x_token)
    if x_token is None:
        raise HTTPException(status_code=401, detail="X-Token header missing")
    # 在这里进行验证 token 的逻辑，这里简单地假设 token 为 "valid_token"
    if x_token != "112334455":
        raise HTTPException(status_code=403, detail="Invalid token")
