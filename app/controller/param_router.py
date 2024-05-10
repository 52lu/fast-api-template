#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：cookie_router.py
@Author  ：Mr.LiuQHui
@Date    ：2024/3/27 22:29
"""
import os
from typing import Annotated
from fastapi import APIRouter, Cookie, Request, Header, Form, UploadFile
from app import utils
from fastapi.responses import FileResponse

router = APIRouter(prefix="/param", tags=["更多参数接收示例"])


@router.get("/cookie/key", summary="接收cookie中指定的key")
async def cookieKey(user_name: Annotated[str | None, Cookie()] = None):
    """接收cookie中指定的key"""
    return {"user_name": user_name}


@router.get("/cookie/all", summary="所有cookie值")
async def cookieParams(request: Request):
    """接收cookie值"""
    return {"cookies": request.cookies}


@router.get("/header/key")
async def headerKey(x_platform: Annotated[str | None, Header()] = None):
    """从header中获取指定key"""
    return {"x_platform": x_platform}


@router.get("/header/keys")
async def headerKey(x_ip: Annotated[list[str] | None, Header()] = None):
    """从header中获取重复key的值"""
    return {"x_ip": x_ip}


@router.post("/form/key")
async def formKey(username: str = Form(), password: str = Form()) -> utils.HttpResponse:
    """接收表单中的参数"""
    body = {"username": username, "password": password}
    return utils.ResponseSuccess(body)


@router.post("/upload/file")
async def uploadFile(
    file: UploadFile | None = None, fileType: str = Form()
) -> utils.HttpResponse:
    """文件上传"""
    if not file:
        return utils.ResponseFail("文件信息不能为空~")

    try:
        # 构造保存目录
        save_path = os.path.join(os.getcwd(), "tmp", fileType)
        # 不存在则创建目录
        os.makedirs(save_path, exist_ok=True)
        # 拼接文件全路径
        file_path = os.path.join(save_path, file.filename)
        # 读取文件内容并写入目标文件
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
        body = {
            "fileName": file.filename,
            "fileType": fileType,
            "size": file.size,
        }
        return utils.ResponseSuccess(body)
    except Exception as e:
        return utils.ResponseFail("文件上传失败:" + str(e))


@router.get("/file/download")
async def downloadFile() -> FileResponse:
    """下载文件"""
    fileName = "test.pdf"
    file_path = os.path.join(os.getcwd(), "tmp", fileName)
    return FileResponse(file_path, filename=fileName)
