## fast-api-template

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.99.0+-00a393?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

### 1.项目介绍

项目是基于[FastAPI](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)
框架搭建的脚手架模板,方便后续其他新项目可以直接使用，但愿该项目能为想学习、想使用FastApi的开发人员提供帮助。



> <span style="color: red; ">@注: 初次学习使用fastapi框架，编码规范和使用方法，仅供参考</span>

- [fastapi中文文档](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)

### 2.目录结构

```shell
├── README.md  #项目介绍
├── app
│   ├── __init__.py
│   ├── config  # 配置相关
│   │   └── __init__.py
│   ├── constant  # 常量相关
│   │   └── __init__.py
│   ├── dao # 封装查询数据的方法
│   │   └── __init__.py
│   ├── dependencies  # 封装被依赖函数
│   │   └── __init__.py
│   ├── main.py # 主文件
│   ├── middleware # 中间件
│   │   └── __init__.py
│   ├── models # 数据模型文件，和表结构对应
│   │   └── __init__.py
│   ├── router # 路由也可以理解controller
│   │   ├── __init__.py
│   │   ├── admin_router.py # 后台接口
│   │   └── demo_router.py # 演示接口
│   ├── parameter # 声明参数对应的Pydantic模型
│   │   └── __init__.py
│   ├── service # 就具体业务实现逻辑
│   │   ├── __init__.py
│   └── utils # 工具类
│       ├── __init__.py
│       └── str_util.py
├── requirements.txt #依赖文件
├── tests # 单元测试目录
    ├── __init__.py
    └── local_test.py
```

### 3.项目启动

```sh
# 使用uvicorn启动
➜ uvicorn app.main:app
INFO:     Started server process [36375]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# 使用python
➜  python main.py
INFO:     Started server process [36468]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 4.项目状态

持续学习开发中...

### 5.项目历程

- [Python框架篇(1):FastApi-快速入门](https://mp.weixin.qq.com/s/AY_MGluXAgr27m2nPByJFw)
- [Python框架篇(2):FastApi-参数接收和验证](https://mp.weixin.qq.com/s/J2_gJxJk2VLfMXgoH1l8Cw)
