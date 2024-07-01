import time

import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd
import func

# 파라미터 종류가 많을 경우 꿀팁
params = {
    "isDetailSearch": "N",
    "searchGubun": "true",
    "viewYn": "OP",
    "strQuery": "패션 인공지능",
    "order": "/DESC",
    "onHanja": "false",
    "strSort": "RANK",
    "iStartCount": "0",
    "fsearchMethod": "search",
    "sflag": "1",
    "isFDetailSearch": "" "N",
    "pageNumber": "1",
    "icate": "re_a_kor",
    "colName": "re_a_kor",
    "pageScale": "100",
    "isTab": "Y",
    "query": "패션 인공지능"
}

response = requests.get("https://www.riss.kr/search/Search.do", params=params)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 나무 태그 찾기
articles = soup.select(".srchResultListW > ul > li")
ic(len(articles))

# for article in articles:
for article in articles[:2]:
    # link = article.select_one("div.cont.ml60 > p.title > a").attrs['href']
    link = "https://www.riss.kr" + article.select_one(".title > a").attrs['href']
    ic(link)
    # print(link)
    # title = article.select_one("div.cont.ml60 > p.title > a").text
    title = article.select_one(".title > a").text
    ic(title)

    ''' 상세 페이지 요청 시작 '''
    # 헤더 추가
    detail_soup = func.get_detail(link)

    press = detail_soup.select_one(".infoDetailL > ul > li:nth-child(2) > div > p > a").text
    ic(press)
    ''' 상세 페이지 요청 끝 '''

    ic("\n\n")
