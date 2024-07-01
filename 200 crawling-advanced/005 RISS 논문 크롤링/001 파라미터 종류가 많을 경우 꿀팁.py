# 1단계
import time

import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd

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
    "isFDetailSearch":"" "N",
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

ic(soup)