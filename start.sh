# !/bin/bash
# 本地测试发布，临时启动脚本
/root/anaconda3/envs/py310/bin/uvicorn app.main:app --host 0.0.0.0 --port 9000 --workers 4