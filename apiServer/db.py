from flask import Blueprint, request, jsonify
import sqlite3
import os

# Blueprint 생성
db_bp = Blueprint('db', __name__)

# 데이터베이스 파일 경로
DB_PATH = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS urls
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             url TEXT NOT NULL,
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        ''')
        conn.commit()
        conn.close()

# 데이터베이스 초기화
init_db()

@db_bp.route('/', methods=['POST'])
def save_url():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "url이 필요합니다"}), 400
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO urls (url) VALUES (?)', (url,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "url이 성공적으로 저장되었습니다"})

@db_bp.route('/urls', methods=['GET'])
def get_urls():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM urls ORDER BY created_at DESC')
    urls = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(urls)

# Blueprint를 명시적으로 export
__all__ = ['db_bp']
