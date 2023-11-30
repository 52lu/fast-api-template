#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template 
@File    ：demo_param.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/16 17:38 
"""
import dataclasses
from enum import Enum
from typing import Union, Optional, List, Dict

# 导入pydantic对应的模型基类
from pydantic import BaseModel, constr, validator, EmailStr, conint, Field
import email_validator


class DemoParam(BaseModel):
    """
    请求体参数对应的模型
    """
    user_name: str | None = Field(default=None, title="用户姓名")
    age: int
    city: Union[str, None]

    class Config:
        """
         参数示例
        """
        schema_extra = {
            "example": {
                "user_name": "张三",
                "age": 89,
                "city": "北京"

            }
        }


class GenderEnum(str, Enum):
    """
    性别枚举
    """
    male = "男"
    female = "女"


class PydanticVerifyParam(BaseModel):
    """
    用来学习使用pydantic模型验证
    """
    user_name: str  # 基本类型
    age: conint(ge=18, le=30)  # 整数范围：18 <= age <= 30
    password: constr(min_length=6, max_length=10)  # 字符长度
    phone: constr(regex=r'^1\d{10}$')  # 正则验证手机号
    address: Optional[str] = None  # 可选参数
    sex: GenderEnum  # 枚举验证,只能传: 男和女
    likes: List[str]  # 值会自动转成传字符串列表
    scores: Dict[str, float]  # key会转成字符串,val 会转成浮点型
    items: List[constr(min_length=1, max_length=3)]  # 限制列表中的每个元素长度的范围
    email: EmailStr  # 邮箱格式

    @validator("user_name")
    def validateUsername(cls, value: str):
        """
        自定义验证函数
        """
        if value.find("傻") > -1:
            raise ValueError("user_name不能包含敏感词")
        return value


class StudentParam(BaseModel):
    """
    学生信息
    """
    name: constr(min_length=2, max_length=4)  # 长度
    age: conint(ge=18, le=30)  # 整数范围：18 <= age <= 30
    class_name: str  # 班级名称


class ClassInfoParam(BaseModel):
    """
    班级信息
    """
    class_name: str  # 班级名称
    class_num: int  # 班级人数
    teacher_name: str  # 老师名称


class FieldParam(BaseModel):
    """
    Field使用示例
    """
    name: str = Field(default=None, title="姓名", max_length=4)
