# 使用官方 Python 基础镜像
FROM python:3.13.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目所有代码到镜像中
COPY . .

# 暴露 FastAPI 默认端口（通常 8000，也可自定义）
EXPOSE 8000

# 启动命令：使用 uvicorn 运行 FastAPI 应用
# 假设入口文件为 main.py，且 app 实例名为 app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]