import requests
import json

# 구글 검색 API 설정
API_KEY = "AIzaSyAXeppgO8IFijBWaIjKejR8wfPK8XqGT-o"
CX = "e453f397eb1f34a7b"

def test_search_api():
    print("\n=== 구글 검색 API 테스트 ===")
    
    # 사용자로부터 검색어 입력 받기
    keyword = input("\n검색어를 입력하세요: ")
    
    # 구글 API 엔드포인트
    url = "https://www.googleapis.com/customsearch/v1"
    
    # API 파라미터
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": keyword
    }
    
    print(f"\n검색어 '{keyword}'로 구글 API 요청을 보내는 중...")
    
    try:
        # API 요청 보내기
        response = requests.get(url, params=params)
        response.raise_for_status()  # HTTP 에러 체크
        
        # 응답 상태 코드 확인
        print(f"\n상태 코드: {response.status_code}")
        
        # 응답 내용 확인
        data = response.json()
        if "items" in data:
            print("\n=== 검색 결과 ===")
            for idx, item in enumerate(data["items"][:5], 1):  # 상위 5개 결과만
                print(f"\n{idx}번째 결과:")
                print(f"제목: {item.get('title', '')}")
                print(f"링크: {item.get('link', '')}")
                print("-" * 50)
        else:
            print("\n검색 결과가 없습니다.")
            
    except requests.exceptions.RequestException as e:
        print(f"\nAPI 요청 중 오류 발생: {str(e)}")
    except Exception as e:
        print(f"\n예상치 못한 에러 발생: {str(e)}")

if __name__ == "__main__":
    while True:
        test_search_api()
        
        # 계속 검색할지 물어보기
        retry = input("\n다시 검색하시겠습니까? (y/n): ").lower()
        if retry != 'y':
            print("\n프로그램을 종료합니다.")
            break 