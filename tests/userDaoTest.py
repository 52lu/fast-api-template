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


if __name__ == '__main__':
    result = dao.UserDao.FindByPhone("17408049453")
    print(result)
