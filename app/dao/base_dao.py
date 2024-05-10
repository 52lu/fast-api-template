#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：baseDao.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/9 23:44
"""
from sqlalchemy import create_engine
from app.config import globalAppSettings
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# 创建引擎
engine = create_engine(
    globalAppSettings.db_dsn,
    echo=globalAppSettings.db_echo_sql,  # 是否打印SQL
    pool_size=globalAppSettings.db_pool_size,  # 连接池的大小，指定同时在连接池中保持的数据库连接数，默认:5
    max_overflow=globalAppSettings.db_max_overflow,  # 超出连接池大小的连接数，超过这个数量的连接将被丢弃,默认: 5
)

# 封装获取会话
Session = sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def getDatabaseSession(autoCommitByExit=True):
    """使用上下文管理资源关闭"""
    _session = Session()
    try:
        yield _session
        # 退出时，是否自动提交
        if autoCommitByExit:
            _session.commit()
    except Exception as e:
        _session.rollback()
        raise e
