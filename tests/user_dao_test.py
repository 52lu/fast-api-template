#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：userDaoTest.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/9 23:22
"""

import unittest
from app import dao


class UserDaoTestCase(unittest.TestCase):
    def test_findByPhone(self):
        """单条查询测试"""
        result = dao.UserDao.findByPhone("17408049453")
        self.assertNotEqual(result.id, 0)

    def test_findByPage(self):
        """分页查询测试"""
        # 10, age=30, gender='male', height=(160, 180), city=['New York', 'Los Angeles']
        total, result = dao.UserDao.findByPage(
            1, 10, id=(10, 30), phone=["17804116371", "17350624789", "17654732912"]
        )
        self.assertNotEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
