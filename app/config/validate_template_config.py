#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：validate_template_config.py
@Author  ：Mr.LiuQHui
@Date    ：2023/12/8 4:34 PM
"""

# 错误模版
validateChineseDict = {
    "value_error.number.not_gt": "{},值不能大于:{}",
    "value_error.number.not_ge": "{},值不能小于等于:{}",
    "value_error.list.min_items": "{},元素个数至少为:{}",
    "value_error.str.regex": "{},不满足规则:{}",
    "value_error.any_str.max_length": "{},最大长度不能超过:{}"
}

# 关键词显示的错误
keyErrorChineseDict = {
    "phone": "手机号格式不正确~"
}
