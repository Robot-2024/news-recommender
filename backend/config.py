# backend/config.py
import os
from dotenv import load_dotenv

# load .env from project root (load_dotenv 默认会查找当前工作目录及其上级的 .env)
load_dotenv()

class Config:
    # DB
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 3306))
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'news_recommender')

    # 请求与爬虫
    USER_AGENT = os.getenv(
        'USER_AGENT',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    )
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 10))

    # 其他
    RETRY_TOTAL = int(os.getenv('RETRY_TOTAL', 3))