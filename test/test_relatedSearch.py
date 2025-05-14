from pytrends.request import TrendReq
import pandas as pd
import time

try:
    # Pytrends 객체 생성
    pytrends = TrendReq(hl='ko-KR', tz=540)

    # 검색어 설정 (더 일반적인 검색어로 변경)
    keyword = ['음식']
    pytrends.build_payload(keyword, cat=0, timeframe='today 5-y', geo='KR')

    # API 요청 간 딜레이 추가
    time.sleep(1)

    # 관련 검색어 요청
    related_queries = pytrends.related_queries()

    # 결과 확인 및 출력
    if related_queries and '음식' in related_queries:
        top_queries = related_queries['음식']['top']
        rising_queries = related_queries['음식']['rising']

        print("'음식' 관련 인기 검색어:")
        print(top_queries)
        print("\n'음식' 관련 급상승 검색어:")
        print(rising_queries)
    else:
        print("'음식' 관련 검색어 결과를 찾을 수 없습니다.")

except Exception as e:
    print(f"오류가 발생했습니다: {str(e)}")