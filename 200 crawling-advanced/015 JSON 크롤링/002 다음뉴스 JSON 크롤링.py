from datetime import datetime

import requests

# API 엔드포인트 URL 설정
url = 'https://news.daum.net/api/harmonydic/contents/news.json'
params = {
    'category': 'economic',
    'approved': 'true',
    'page': '1',
    'pageSize': '20',
    'pagesToShow': '10',
    'range': '1'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json',
}

# HTTP 요청 보내기
response = requests.get(url, headers=headers, params=params)
data = response.json()

print(data)

# 기사 정보 추출
articles = []
for item in data['list']:
    title = item['title']
    link = item['contentUrl']
    press = item['cpKorName']
    date = item['regDt']

    # 날짜 형식 변환
    date_object = datetime.fromtimestamp(date / 1000)  # milliseconds to seconds
    formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S')

    articles.append({
        'title': title,
        'link': link,
        'press': press,
        'date': formatted_date
    })

# 결과 출력
for article in articles:
    print(f"제목: {article['title']}")
    print(f"링크: {article['link']}")
    print(f"언론사: {article['press']}")
    print(f"날짜: {article['date']}\n")
