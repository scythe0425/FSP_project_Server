from flask import Blueprint, request, jsonify
import webbrowser
import keyboard
import time
from db import save_url

chrome_bp = Blueprint('chrome', __name__)

@chrome_bp.route('/', methods=['POST'])
def chrome():
    data = request.get_json()
    keyword = data.get('keyword')
    return jsonify({"message": "Chrome 호출 성공"})

@chrome_bp.route('/open', methods=['POST'])
def open_url():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL이 필요합니다"}), 400
        
    try:
        webbrowser.open(url)
        return jsonify({"message": "URL이 성공적으로 열렸습니다"})
    except Exception as e:
        return jsonify({"error": f"URL을 여는 중 오류 발생: {str(e)}"}), 500
