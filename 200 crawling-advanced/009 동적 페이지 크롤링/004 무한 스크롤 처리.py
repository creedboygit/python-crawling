import time

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
