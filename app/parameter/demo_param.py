#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template 
@File    ：demo_param.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/16 17:38 
"""
from typing import Union

# 导入pydantic对应的模型基类
from pydantic import BaseModel


class DemoParam(BaseModel):
    """
    请求体参数对应的模型
    """
    user_name: str
    age: int
    city: Union[str, None]
