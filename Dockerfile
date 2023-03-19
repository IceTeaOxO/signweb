# 基礎映像檔
FROM python:3.11.1-slim-buster

# 將工作目錄設置為 /app
WORKDIR /app

# 複製必要的檔案到映像檔中
COPY . /app

# 安裝必要的套件
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5000

# 運行 Flask 應用程序
CMD ["python", "app.py"]