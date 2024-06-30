# 1단계
# 1번째 글 - 제목, 링크, 날짜, 카테고리, 답변수
import time

import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd

response = requests.get("https://kin.naver.com/search/list.naver?query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

title = soup.select_one("._nclicks\\:kin\\.txt").text.strip()
ic(title)

title = soup.select_one("._searchListTitleAnchor").text.strip()
ic(title)

title_select = soup.select_one("._nclicks\\:kin\\.txt._searchListTitleAnchor")
title = title_select.text.strip()
ic(title)

link = title_select.attrs['href']
ic(link)

date = soup.select_one(".txt_inline").text
ic(date)

data_block = soup.select_one(".txt_block").contents
ic(data_block)

ic(data_block[1].text)
ic(data_block[3].text)

category = data_block[1].text + " > " + data_block[3].text
ic(category)

reply_count = data_block[7].text.split(" ")[1]
ic(reply_count)

