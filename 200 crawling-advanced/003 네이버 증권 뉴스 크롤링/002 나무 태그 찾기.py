# 2단계
# 1페이지 20개 뉴스 - 제목, 링크, 내용, 언론사, 날짜 출력
import requests
from bs4 import BeautifulSoup
from icecream import ic

response = requests.get("https://finance.naver.com/news/mainnews.naver?date=2024-06-26")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

articles = soup.select(".block1")

for item in articles:
    select_dl = item.select_one(".block1 > dl")

    # 썸네일
    thumb = select_dl.select_one(".thumb > a > img").attrs["src"]
    ic.disable()
    ic(thumb)

    # 제목
    title = select_dl.select_one(".articleSubject").text.strip()
    ic(title)

    # 링크
    link = "https://finance.naver.com" + select_dl.select_one(".articleSubject > a").attrs["href"]
    ic(link)

    # 내용
    articleSummary_dd = select_dl.select_one(".articleSummary").contents
    # ic(articleSummary_dd)

    contents = articleSummary_dd[0].strip()
    ic(contents)

    press = articleSummary_dd[1].text.strip()
    ic(press)

    date = select_dl.select_one(".wdate").text.strip()
    ic(date)

    ic.enable()
    ic(thumb, title, link, contents, press, date)

    ic("\n\n")


#
# title = select.text
# link = select.attrs['href']
# link = "https://finance.naver.com" + link
# print(title, link)
# # content = soup.select_one(".articleSummary").contents[0].strip()
# contents_data = soup.select_one(".articleSummary")
# print(contents_data)
# contents = contents_data.contents[0].strip()
# press = contents_data.select_one(".press").text.strip()
# wdate = contents_data.select_one(".wdate").text.strip()
# print(contents)
# print(press)
# print(wdate)




