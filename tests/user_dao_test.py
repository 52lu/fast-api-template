#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：userDaoTest.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/9 23:22
"""

import unittest
from datetime import datetime

from app import dao
from app.dao import models


class UserDaoTestCase(unittest.TestCase):
    def test_findByPhone(self):
        """单条查询测试"""
        result = dao.UserQueryDao.findByPhone("17408049453")
        self.assertNotEqual(result.id, 0)

    def test_findByPage(self):
        """分页查询测试"""
        # 10, age=30, gender='male', height=(160, 180), city=['New York', 'Los Angeles']
        total, result = dao.UserQueryDao.findByPage(
            1,
            10,
            id=(10, 30),
            phone=["17804116371", "17350624789", "17654732912", "17545435626"],
            nick_name="%雨%",
        )
        self.assertNotEqual(len(result), 0)

    def test_saveUser(self):
        """单条查询测试"""
        result = dao.UserOperateDao.saveUser(
            models.YmUser(
                union_id="ui_12344343434",
                open_id="op_ksjdhjjkdhdjdhh",
                nick_name="娃哈哈",
                password="123456",
                email="test@163.com",
                phone="17600000000",
                last_login=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                avatar="http://img-avatar.com/head-abc.jpg",
            )
        )
        print(result.id)
        self.assertNotEqual(result.id, 0)


if __name__ == "__main__":
    unittest.main()
