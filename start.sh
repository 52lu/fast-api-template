# !/bin/bash
# 临时启动脚本
uvicorn app.main:app --host 0.0.0.0 --port 9000 --workers 4