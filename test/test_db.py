from db import save_url, get_all_urls
import time

def test_db():
    print("=== DB 테스트 시작 ===")
    
    # 테스트할 URL들
    test_urls = [
        "https://www.google.com",
        "https://www.naver.com",
        "https://www.youtube.com"
    ]
    
    # URL 저장 테스트
    print("\n1. URL 저장 테스트")
    for url in test_urls:
        try:
            save_url(url)
            print(f"URL 저장 성공: {url}")
            time.sleep(0.5)  # DB 작업 간격을 두기 위해
        except Exception as e:
            print(f"URL 저장 실패: {url}")
            print(f"에러: {str(e)}")
    
    # 저장된 URL 조회 테스트
    print("\n2. 저장된 URL 조회 테스트")
    try:
        urls = get_all_urls()
        print("저장된 URL 목록:")
        for url in urls:
            print(f"- {url}")
    except Exception as e:
        print(f"URL 조회 실패")
        print(f"에러: {str(e)}")
    
    print("\n=== DB 테스트 완료 ===")

if __name__ == "__main__":
    test_db() 