from flask import Blueprint, request, jsonify
import requests

search_bp = Blueprint('search', __name__)

API_KEY = "AIzaSyAXeppgO8IFijBWaIjKejR8wfPK8XqGT-o"
CX = "e453f397eb1f34a7b"

@search_bp.route('/', methods=['POST'])
def search():
    data = request.get_json()
    keyword = data.get('keyword')
    
    if not keyword:
        return jsonify({"error": "검색어가 필요합니다"}), 400

    try:
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            "key": API_KEY,
            "cx": CX,
            "q": keyword
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # 검색 결과 처리
        if "items" in data:
            results = []
            for item in data["items"][:10]:
                results.append({
                    "title": item.get("title", ""),
                    "link": item.get("link", "")
                })
            return jsonify(results)
        else:
            return jsonify({"error": "검색 결과가 없습니다"}), 404
            
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API 요청 중 오류 발생: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"처리 중 오류 발생: {str(e)}"}), 500
