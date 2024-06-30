# 3단계
# 1페이지 ~ 마지막 페이지 크롤링하기
import time

import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd

data = []
for page in range(9, 1000):
    response = requests.get(f"https://finance.naver.com/news/mainnews.naver?date=2024-06-26&page={page}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.select(".block1")

    ic(page)

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

        data.append([thumb, title, link, contents, press, date])

        ic("\n\n")

    time.sleep(1)

    # 맨 마지막 페이지라면 break
    pgRR = soup.select_one(".pgRR")
    ic(pgRR)
    if pgRR == None:
        break

# 데이터 프레임 생성
df = pd.DataFrame(data, columns=['썸네일', '제목', '링크', '내용', '언론사', '날짜'])

# 엑셀 저장
# df.to_excel("naver_finance_crawling.xlsx")

# 한글 깨짐 방지, index 번호 컬럼 미노출
df.to_csv("naver_finanace_crawling.csv", index=False, encoding="utf-8-sig")

