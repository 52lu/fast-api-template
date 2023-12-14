#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：jwt_util.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/14 12:06 PM
"""
from datetime import datetime, timedelta
from typing import Any

import jwt
from pydantic import BaseModel

from app import constant


class JwtTokenBody(BaseModel):
    """ jwt数据格式"""
    jti: str  # 签发唯一编号
    iss: str  # 签发人
    iat: datetime  # 签发时间
    exp: datetime  # 过期时间
    data: Any  # 业务数据


# token过期
TokenErrorTimeOut = "TokenTimeOut|token过期"
# token非法
TokenErrorInvalid = "TokenInvalid|token非法"


class JwtManageUtil(object):
    """
    JWT处理类
    """

    def __init__(self, secretKey: str, algorithm: str = "HS256", expired: int = 60,
                 chinaTimeZone=constant.ChinaTimeZone, iss: str = "猿码记"):
        """
        初始化
        :param secretKey: 秘钥
        :param algorithm: 算法
        :param expired: 过期时间(单位:分钟)
        """
        self.secretKey = secretKey
        self.algorithm = algorithm
        self.expired = expired
        self.iss = iss
        self.chinaTimeZone = chinaTimeZone

    def generate(self, payload: BaseModel) -> str:
        """
        生成 JWT
        :param payload: JwtTokenParam
        :return: str
        """
        # 当前时间 一定要设置时区，否则解析会报错： The token is not yet valid (iat)
        currentTime = datetime.now(self.chinaTimeZone)
        jwtData = JwtTokenBody(
            jti=currentTime.strftime("%Y%m%d%H%M%f"),
            iss=self.iss,
            iat=currentTime,
            exp=currentTime + timedelta(minutes=self.expired),
            data=payload
        )
        # 生成 JWT
        return jwt.encode(jwtData.dict(), self.secretKey, algorithm=self.algorithm)

    def decode(self, jwtToken: str, decodePydanticModel: Any) -> BaseModel | str:
        """
        解析 jwtToken
        :param jwtToken: str
        :param decodePydanticModel: BaseModel
        :return: BaseModel | bool
        """
        try:
            decoded_payload = jwt.decode(jwtToken, self.secretKey, algorithms=[self.algorithm])
            result = JwtTokenBody(**decoded_payload)
            return decodePydanticModel.parse_obj(result.data)
        except jwt.ExpiredSignatureError:
            return TokenErrorTimeOut
        except jwt.InvalidTokenError:
            return TokenErrorInvalid
        except Exception as e:
            return str(e)
