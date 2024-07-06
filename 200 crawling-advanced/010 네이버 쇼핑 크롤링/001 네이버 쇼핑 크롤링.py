import time

from bs4 import BeautifulSoup
from icecream import ic
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

### ChromeOptions 객체 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

### 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

### 페이지 이동
# driver.get("https://search.shopping.naver.com/search/all?query=%EC%9D%B4%EC%96%B4%ED%8F%B0")
driver.get("https://search.shopping.naver.com/search/all?query=이어폰")


##### 무한 스크롤 - 시작
### 스크롤 전 높이 확인
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    ### 스크롤 끝까지 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 대기 시간 꼭 주기
    time.sleep(1)

    ### 스크롤 후 높이
    new_height = driver.execute_script("return document.body.scrollHeight")

    ### 스크롤 전, 스크롤 후 높이 비교 (if, break)
    if new_height == last_height:
        break

    ### 스크롤 전 높이 업데이트
    last_height = new_height
##### 무한 스크롤 - 종료


##### 상품명, 상세페이지 링크, 가격 추출 - 시작
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

items = soup.select(".product_item__MDtDF")
# ic(items)

result = []
for item in items:
    name = item.select_one(".product_title__Mmw2K > a").text
    link = item.select_one(".product_title__Mmw2K > a").attrs["href"]
    # price = item.select_one("div > div > div.product_info_area__xxCTi > div.product_price_area__eTg7I > strong > span.price > span.price_num__S2p_v > em").text
    # ic(price)
    # price = item.select_one("span.price_num__S2p_v").text.split('원')[0].replace(',', '').strip()
    price = int(item.select_one("span.price_num__S2p_v").text.replace('원', '').replace(',', '').strip())
    # ic(name, link, price)
    result.append([name, link, price])

##### 상품명, 상세페이지 링크, 가격 추출 - 종료

##### 엑셀 저장 - 시작
df = pd.DataFrame(result, columns=['상품명', '상세페이지링크', '가격'])
df.to_excel('result.xlsx', index=False)
##### 엑셀 저장 - 종료
