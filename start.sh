# !/bin/bash
# 本地测试发布，临时启动脚本
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1