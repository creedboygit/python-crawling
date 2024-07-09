import requests
from datetime import datetime


def fetch_daum_news():
    url = "https://news.daum.net/api/harmonydic/contents/news.json"
    params = {
        "category": "economic",
        "approved": "true",
        "page": "1",
        "pageSize": "20",
        "pagesToShow": "10",
        "range": "1"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://news.daum.net/economic"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        news_data = response.json()
        print(news_data)

        for item in news_data.get("list", []):
            try:
                title = item.get("title", "제목 없음")
                link = item.get("contentUrl", "링크 없음")
                press = item.get("cpKorName", "언론사 정보 없음")
                timestamp = item.get("regDt")

                if timestamp:
                    date_object = datetime.fromtimestamp(timestamp / 1000)
                    formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    formatted_date = "날짜 정보 없음"

                print(f"제목: {title}")
                print(f"링크: {link}")
                print(f"언론사: {press}")
                print(f"생성날짜: {formatted_date}")
                print("-" * 50)
            except Exception as e:
                print(f"항목 처리 중 오류 발생: {e}")
                continue

    except requests.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")
    except ValueError as e:
        print(f"JSON 파싱 중 오류 발생: {e}")
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")


if __name__ == "__main__":
    fetch_daum_news()
