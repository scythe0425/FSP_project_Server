from flask import Blueprint, request, jsonify
import webbrowser
import keyboard
import time
from db import get_db_connection
from url_manager import url_bp

chrome_bp = Blueprint('chrome', __name__)

@chrome_bp.route('/open/category/<category>', methods=['POST'])
def open_urls_by_category(category):
    conn = None
    try:
        # 카테고리에 해당하는 모든 URL 열기
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT url FROM urls WHERE category = ?', (category,))
        urls = [row['url'] for row in c.fetchall()]
        
        if not urls:
            return jsonify({"error": f"'{category}' 카테고리에 해당하는 URL이 없습니다"}), 404
        
        # 모든 URL 열기
        for url in urls:
            try:
                webbrowser.open(url)
            except Exception as e:
                return jsonify({"error": f"URL '{url}'을 여는 중 오류 발생: {str(e)}"}), 500
        
        return jsonify({
            "message": f"'{category}' 카테고리의 {len(urls)}개 URL이 성공적으로 열렸습니다",
            "urls": urls
        })
            
    except Exception as e:
        return jsonify({"error": f"처리 중 오류 발생: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

@chrome_bp.route('/open/id/<int:url_id>', methods=['POST'])
def open_url(url_id):
    conn = None
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM urls WHERE id = ?', (url_id,))
        url = c.fetchone()

        if not url:
            return jsonify({"error": "URL을 찾을 수 없습니다"}), 404
            
        try:
            webbrowser.open(url['url'])
            return jsonify({"message": "URL이 성공적으로 열렸습니다"})
        except Exception as e:
            return jsonify({"error": f"URL을 여는 중 오류 발생: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
