from pytrends.request import TrendReq
import pandas as pd


pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, requests_args={'verify':False})

# 검색어 설정: 'apple'
keyword = ['apple']

# 관련 검색어 요청
related_queries = pytrends.related_queries()

# 결과 확인 및 출력
if related_queries and 'apple' in related_queries:
    if 'top' in related_queries['apple'] and not related_queries['apple']['top'].empty:
        top_queries = related_queries['apple']['top']
        print("'apple' 관련 인기 급상승 검색어:")
        print(top_queries)
    else:
        print("'apple' 관련 인기 급상승 검색어 결과가 없습니다.")

    if 'rising' in related_queries['apple'] and not related_queries['apple']['rising'].empty:
        rising_queries = related_queries['apple']['rising']
        print("\n'apple' 관련 급상승 검색어:")
        print(rising_queries)
    else:
        print("\n'apple' 관련 급상승 검색어 결과가 없습니다.")
else:
    print("'apple' 관련 검색어 결과를 찾을 수 없습니다.")
