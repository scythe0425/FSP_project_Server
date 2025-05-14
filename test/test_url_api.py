import requests
import json

def test_update_category():
    # API 엔드포인트
    url = "http://127.0.0.1:5001/url/update/1/category"
    
    # 요청 데이터
    data = {
        "category": "테스트카테고리"
    }
    
    try:
        # PUT 요청 보내기
        response = requests.put(url, json=data)
        
        # 응답 확인
        print(f"상태 코드: {response.status_code}")
        print(f"응답 내용: {response.json()}")
        
    except requests.exceptions.ConnectionError:
        print("서버에 연결할 수 없습니다. 서버가 실행 중인지 확인해주세요.")
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    test_update_category() 