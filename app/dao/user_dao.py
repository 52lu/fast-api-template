#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：userDao.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/9 16:17
"""
from sqlalchemy import desc

from .base_dao import getDatabaseSession
from app.dao.models import YmUser


class UserQueryDao(object):
    """用户查询类dao"""

    @classmethod
    def findByPhone(cls, phone: str) -> YmUser:
        """单条查询示例"""
        with getDatabaseSession() as session:
            query = session.query(YmUser).filter(YmUser.phone == phone)
            result = query.first()
        return result

    @classmethod
    def findByPage(cls, page: int = 1, pageSize: int = 10, **kwargs) -> (int, list[YmUser]):
        """分页查询示例"""
        with getDatabaseSession() as session:
            query = session.query(YmUser)
            # 填充具体查询条件
            for column, value in kwargs.items():
                if not hasattr(YmUser, column):
                    continue

                # 根据值类型，来组装查询条件
                if isinstance(value, tuple):
                    # 范围查询
                    query = query.filter(getattr(YmUser, column).between(*value))
                elif isinstance(value, list):
                    # in查询
                    query = query.filter(getattr(YmUser, column).in_(value))
                elif isinstance(value, str) and value.find("%") != -1:
                    # 模糊查询
                    query = query.filter(getattr(YmUser, column).like(value))
                else:
                    # 等值查询
                    query = query.filter(getattr(YmUser, column) == value)

            # 查询总条数
            total = query.count()
            # 排序分页
            offset = (page - 1) * pageSize
            query = query.order_by(desc(YmUser.id)).offset(offset).limit(pageSize)
            # 查询记录
            result = query.all()

        return total, result


class UserOperateDao(object):
    """操作用户相关dao"""

    @classmethod
    def saveUser(cls, user: YmUser) -> YmUser:
        """添加单条"""
        with getDatabaseSession(False) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    @classmethod
    def saveUserList(cls, users: list[YmUser]):
        """添加单条"""
        with getDatabaseSession() as session:
            session.bulk_save_objects(users)
        return
