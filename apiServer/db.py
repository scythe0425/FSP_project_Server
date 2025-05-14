import sqlite3
import os
from flask import Blueprint

db_bp = Blueprint('db', __name__)

# 데이터베이스 파일 경로
DB_PATH = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# 데이터베이스 초기화
def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS urls
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             url TEXT NOT NULL,
             category TEXT,
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        ''')
        conn.commit()
        conn.close()

init_db()

__all__ = ['db_bp'] 