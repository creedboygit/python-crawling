# 1단계
# 첫번째 뉴스 - 제목, 링크, 내용, 언론사, 날짜
import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/news/mainnews.naver?date=2024-06-26")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

select = soup.select_one(".articleSubject > a")
title = select.text
link = select.attrs['href']
link = "https://finance.naver.com" + link
print(title, link)
# content = soup.select_one(".articleSummary").contents[0].strip()
contents_data = soup.select_one(".articleSummary")
print(contents_data)
contents = contents_data.contents[0].strip()
press = contents_data.select_one(".press").text.strip()
wdate = contents_data.select_one(".wdate").text.strip()
print(contents)
print(press)
print(wdate)




