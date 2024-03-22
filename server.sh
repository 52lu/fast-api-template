#!/bin/bash
# 设置 FastAPI 应用程序的文件路径和名称
APP_FILE="main.py"
# 临时目录
TMP_PATH="./tmp"

# 可以写本地具体路径 如:/usr/bin/python
PYTHON_BIN="python"

# 默认参数
DEFAULT_UVICORN_OPTS=""

# 启动 FastAPI 应用程序
start() {
    echo "准备启动应用程序..."
    echo "运行脚本: $PYTHON_BIN $APP_FILE $DEFAULT_UVICORN_OPTS $@"
    $PYTHON_BIN $APP_FILE $DEFAULT_UVICORN_OPTS "$@" &
    echo $! > $TMP_PATH/app.pid
}

# 重启 FastAPI 应用程序
restart() {
    echo "准备重启应用程序..."
    stop
    start "$@"
}

# 关闭 FastAPI 应用程序
stop() {
    echo "准备关闭应用程序..."
    if [ -f $TMP_PATH/app.pid ]; then
        pid=$(cat $TMP_PATH/app.pid)
        kill $pid
        rm $TMP_PATH/app.pid
    else
        echo "PID file not found. Service might not be running."
    fi
}

# 解析命令行参数
case "$1" in
    start)
        shift
        start "$@"
        ;;
    restart)
        shift
        restart "$@"
        ;;
    stop)
        stop
        ;;
    *)
        echo "Usage: $0 {start|restart|stop}"
        exit 1
        ;;
esac

