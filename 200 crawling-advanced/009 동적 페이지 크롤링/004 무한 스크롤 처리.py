import time

from bs4 import BeautifulSoup
from icecream import ic
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

### ChromeOptions 객체 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

### 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

### 페이지 이동
driver.get("https://startcoding.pythonanywhere.com/dynamic")

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

#### 시작 - 데이터 추출
source = driver.page_source
soup = BeautifulSoup(source, "lxml")

items = soup.select(".product")
for item in items:
    category = item.select_one(".product-category").text
    name = item.select_one(".product-name").text
    link = item.select_one(".product-name > a").attrs["href"]
    price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
    ic(category, name, link, price)
#### 종료 - 데이터 추출
