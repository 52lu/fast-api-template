#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：api.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 11:45 
"""
from fastapi import APIRouter
from fastapi import Response

from app.utils import httputil
from app.config import appSettings
from app.service.aiservice import aitext

router = APIRouter()


@router.get("/")
async def index():
    return httputil.HttpSuccess(appSettings)


@router.get("/text2img/")
async def text2img(text: str):
    if text == "":
        return httputil.HttpFail("参数不能为空~")
    imgName = aitext.textToImg(text)
    with open(imgName, "rb") as img_file:
        imgData = img_file.read()
    return Response(content=imgData, media_type="image/jpeg")
    # return httputil.HttpSuccess(text)
