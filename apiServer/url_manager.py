from flask import Blueprint, request, jsonify
from db import get_db_connection

# Blueprint 생성
url_bp = Blueprint('url', __name__)

# URL 저장
@url_bp.route('/', methods=['POST'])
def save_url():
    data = request.get_json()
    url = data.get('url')
    category = data.get('category')
    
    if not url:
        return jsonify({"error": "url이 필요합니다"}), 400
    if not category:
        category = 'default'

    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO urls (url, category) VALUES (?, ?)', (url, category))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "URL saved successfully", "url": url, "category": category})

# URL 조회
@url_bp.route('/', methods=['GET'])
def get_urls():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT url, created_at FROM urls ORDER BY created_at DESC')
    urls = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(urls)

# 카테고리별 URL 조회
@url_bp.route('/category/<category>', methods=['GET'])
def get_urls_by_category(category):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM urls WHERE category = ? ORDER BY created_at DESC', (category,))
    urls = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(urls)

# URL 카테고리 업데이트
@url_bp.route('/update/<int:url_id>/<new_category>', methods=['PUT'])
def update_category(url_id, new_category):
    if not new_category:
        return jsonify({"error": "새로운 카테고리가 필요합니다"}), 400

    conn = get_db_connection()
    c = conn.cursor()

    # URL이 존재하는지 확인
    c.execute('SELECT * FROM urls WHERE id = ?', (url_id,))
    url = c.fetchone()

    if not url:
        conn.close()
        return jsonify({"error": "해당 URL을 찾을 수 없습니다"}), 404

    # 카테고리 업데이트
    c.execute('UPDATE urls SET category = ? WHERE id = ?', (new_category, url_id))
    conn.commit()
    conn.close()

    return jsonify({
        "message": "category updated successfully",
        "url_id": url_id,
        "new_category": new_category
    })

# URL 삭제
@url_bp.route('/<int:url_id>', methods=['DELETE'])
def delete_url(url_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM urls WHERE id = ?', (url_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "URL deleted successfully"})






# Blueprint를 명시적으로 export
__all__ = ['url_bp'] 