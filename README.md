## fast-api-template

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-00a393?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

### 1.项目介绍

项目是基于[FastAPI](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)
学习使用FastAPI框架，并搭建一个项目模板,方便后续其他新项目可以直接使用，但愿该项目能为想学习、想使用FastApi的开发人员提供帮助。

> <span style="color: red; ">@提示:
> 由于本人工作中常用的语言是PHP和Go，所以框架中的编码规范，并没有严格按照Python官方指定的规范，特别是变量名和函数名~</span>

- [fastapi中文文档](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)

### 2.目录结构

> <span style="color: red; ">@注: 下面目录仅供参考，在整个项目未开发结束,会有部分调整。</span>

```shell
├── app
│   ├── __init__.py
│   ├── config  # 配置相关
│   │   └── __init__.py
│   ├── constant  # 常量相关
│   │   └── __init__.py
│   ├── dao # 封装查询数据的方法
│   │   ├── models # 数据模型文件，和表结构对应
│   │   └── __init__.py
│   ├── dependencies  # 封装被依赖函数
│   │   └── __init__.py
│   ├── errors  # 异常处理
│   │   └── __init__.py
│   ├── middleware # 中间件
│   │   └── __init__.py
│   ├── router # 路由也可以理解controller
│   │   ├── __init__.py
│   │   ├── admin_router.py # 后台接口
│   │   └── demo_router.py # 演示接口
│   ├── types # 声明入参和出参对应的Pydantic模型
│   │   ├── __init__.py
│   │   ├── request # 入参模型
│   │   └── response # 出参模型
│   ├── service # 就具体业务实现逻辑
│   │   ├── __init__.py
│   └── utils # 工具类
│       ├── __init__.py
│       └── str_util.py
├── bin # 相关脚本
│   ├── genmodels.sh # 生成model脚本
│   └── updateRequirements.sh # 更新项目依赖脚本
├── logs # 日志目录
│   └── app.log
├── static # 静态资源目录
│   ├── a.txt
│   └── test.jpg
├── requirements.txt #依赖文件
├── README.md  #项目介绍
├── main.py # 入口文件
└── tests # 单元测试目录
    ├── __init__.py
    └── local_test.py
```

### 3.项目启动

#### 3.1 安装依赖

```shell
➜ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 3.2 服务启动

```sh
# 启动: 可指定 环境配置文件test(.env.test)、prod(.env.prod)
➜  ./server.sh start --env=test
准备启动应用程序...
运行脚本: python main.py  --env=test
获取配置文件:  .env.test
打印项目配置: ...
INFO:     Started server process [36836]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8082 (Press CTRL+C to quit)

# 关闭
➜  ./server.sh stop 

# 重启
➜  ./server.sh restart 
```

### 4.项目状态

持续学习开发中...

### 5.项目历程  

- [Python框架篇(1):FastApi-快速入门](https://mp.weixin.qq.com/s/AY_MGluXAgr27m2nPByJFw)
- [Python框架篇(2):FastApi-参数接收和验证](https://mp.weixin.qq.com/s/J2_gJxJk2VLfMXgoH1l8Cw)
- [Python框架篇(3):FastApi-响应模型](https://mp.weixin.qq.com/s/okmkZXWZ3qwS1cnAceky0w)
- [Python框架篇(4):FastApi-错误处理](https://mp.weixin.qq.com/s/W6TxoQ_i-CUCKRhorZReaw)
- [Python框架篇(5):FastApi-中间件使用](https://mp.weixin.qq.com/s/2MFPnly7pv_dhKT3zGw3VA)
- [Python框架篇(6):FastApi-配置管理](https://mp.weixin.qq.com/s/3TQYLGebfsEmZt_FQBIV1Q)
- [Python框架篇(7):FastApi-依赖项](https://mp.weixin.qq.com/s/UvTytHAkC2bue-1ee6Ib1w)
- [Python框架篇(8):FastApi-文件处理](https://mp.weixin.qq.com/s/zOxkbJkDoQCA0fCkWGF00Q)

