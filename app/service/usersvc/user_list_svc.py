#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：user_list_svc.py
@Author  ：Mr.LiuQHui
@Date    ：2024/5/10 17:45
"""
from typing import List

from app.types import apiproto
from app import dao


class UserListService:
    """用户列表"""

    @classmethod
    def getUserList(cls, queryParam: apiproto.UserListRequest) -> apiproto.UserListResponse:
        """查询用户列表"""

        # 拼凑查询信息
        queryDict = {}
        if queryParam.nick_name != "":
            queryDict["nick_name"] = f"%{queryParam.nick_name}%"
        if queryParam.phone != "":
            queryDict["phone"] = queryParam.phone

        total, result = dao.UserQueryDao.findByPage(
            queryParam.page,
            queryParam.pageSize,
            **queryDict
        )
        if total == 0:
            return apiproto.UserListResponse()

        # 格式化数据
        records_list: List[apiproto.UserDetailProto] = []

        for record in result:
            tmp = apiproto.UserDetailProto(
                id=record.id,
                union_id=record.union_id,
                open_id=record.open_id,
                nick_name=record.nick_name,
                avatar=record.avatar,
                phone=record.phone,
                email=record.email,
                last_login=record.last_login,
                status=record.status,
                delete_at=record.delete_at,
                created_at=str(record.created_at),
                updated_at=str(record.updated_at),
            )
            records_list.append(tmp)

        return apiproto.UserListResponse(record_total=total, record_list=records_list)
