import requests
import json


def fetch_news_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청 오류를 체크합니다.
        data = response.json()  # JSON 데이터로 디코딩합니다.
        print(data)
        return data['list']  # 'data' 키에 있는 실제 데이터를 반환합니다.
    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청 오류: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON 디코딩 오류: {e}")
        return None


def print_news_details(news_list):
    for news in news_list:
        title = news.get('title', '제목 없음')
        link = news.get('contentUrl', '링크 없음')
        cp_name = news.get('cpKorName', '언론사 없음')
        input_date = news.get('regDt', '날짜 없음')

        print(f"제목: {title}")
        print(f"링크: {link}")
        print(f"언론사: {cp_name}")
        print(f"생성날짜: {input_date}")
        print("---------------------")


if __name__ == "__main__":
    url = "https://news.daum.net/api/harmonydic/contents/news.json"
    news_data = fetch_news_data(url)

    if news_data:
        print_news_details(news_data)
