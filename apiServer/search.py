from flask import Blueprint, request, jsonify

search_bp = Blueprint('search', __name__)

@search_bp.route('/', methods=['POST'])
def search():
    data = request.get_json()
    keyword = data.get('keyword')

    # 여기에 구글 API 요청 로직 작성
    result = f"{keyword} 검색 결과"  # 예시

    return jsonify({'result': result})
