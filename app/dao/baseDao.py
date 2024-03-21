#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：baseDao.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/19 21:54
"""

from contextlib import contextmanager

from app.initialize import GlobalSessionLocal


@contextmanager
def getSession(autoCommitByExit=True):
    """使用上下文管理资源关闭"""
    session = GlobalSessionLocal()
    try:
        yield session
        # 退出时，是否自动提交
        if autoCommitByExit:
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
