#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：userDao.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/9 16:17
"""
from .baseDao import getDatabaseSession
from app.dao import models


class UserDao(object):
    @classmethod
    def FindByPhone(cls, phone: str):
        """ 查询示例 """
        with getDatabaseSession() as session:
            query = session.query(models.YmUser).filter(
                models.YmUser.phone == phone
            )
            result = query.first()
            print(result)
        return result
