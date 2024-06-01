# 使用 Python 官方的輕量級 Alpine 映像
FROM python:3.10.14-alpine3.18

# 設置工作目錄
WORKDIR /app

# 複製當前目錄的內容到工作目錄
COPY . /app

# 安裝構建工具和升級 pip
RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# 設置執行指令
CMD ["python", "app/test.py"]
