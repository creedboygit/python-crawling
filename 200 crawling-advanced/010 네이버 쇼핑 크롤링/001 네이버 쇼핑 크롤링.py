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

    ## 상품명
    name = item.select_one(".product_title__Mmw2K > a").text

    ## 링크
    link = item.select_one(".product_title__Mmw2K > a").attrs["href"]

    ## 가격
    # price = item.select_one("div > div > div.product_info_area__xxCTi > div.product_price_area__eTg7I > strong > span.price > span.price_num__S2p_v > em").text
    # ic(price)
    # price = item.select_one("span.price_num__S2p_v").text.split('원')[0].replace(',', '').strip()
    price = int(item.select_one("span.price_num__S2p_v").text.replace('원', '').replace(',', '').strip())

    ### 구매건수
    ## 속성 선택자로 구매건수 추출
    ## [data - nclick *= purchase] > span > span > em
    ## 후손선택자 : [data-nclick*=purchase] em 로 표현 가능
    if item.select_one("[data-nclick*=purchase] em"):  # 구매건수가 존재하면
        purchase = item.select_one("[data-nclick*=purchase] em").text.replace(',', '')

        ## 1.4만 등의 문자열 숫자로 전처리
        if '만' in purchase:
            ic(float(purchase.split('만')[0]))
            purchase = int(float(purchase.split('만')[0]) * 10000)
    else:
        purchase = ''

    ic(name, link, price, purchase)
    result.append([name, link, price, purchase])

##### 상품명, 상세페이지 링크, 가격 추출 - 종료

##### 엑셀 저장 - 시작
df = pd.DataFrame(result, columns=['상품명', '상세페이지링크', '가격', '구매건수'])
df.to_excel('result.xlsx', index=False)
##### 엑셀 저장 - 종료
