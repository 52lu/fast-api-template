#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-use-ai 
@File    ：aitext.py
@Author  ：Mr.LiuQHui
@Date    ：2023/8/10 18:20 
"""
import time

import requests
import io
from PIL import Image
from app.config import appSettings


def textToImg(text: str) -> str:
    """
    文字转成图片
    :param text:
    :return:
    """
    API_URL = "https://api-inference.huggingface.co/models/IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-v0.1"
    headers = {"Authorization": "Bearer {}".format(appSettings.hugging_face_token)}
    # 入参
    param = {
        "inputs": text,
    }
    response = requests.post(API_URL, headers=headers, json=param)
    image = Image.open(io.BytesIO(response.content))
    imgName = "{}/{}.jpg".format(appSettings.img_path, time.time())
    image.save(imgName)
    return imgName
