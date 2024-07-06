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
driver.get("https://cafe.naver.com/joonggonara")

### 중고나라 > 여성패션/잡화 게시판 클릭 id: menuLink356
driver.find_element(By.CSS_SELECTOR, "#menuLink356").click()

### iframe으로 전환하기
iframe = driver.find_element(By.CSS_SELECTOR, "#cafe_main")
driver.switch_to.frame(iframe)

time.sleep(1)

### 50개씩 표시하기 클릭
## ElementNotInteractableException : 50개씩보기 태그가 보이지 않아서 클릭할 수 없어서 나오는 오류
element = driver.find_element(By.CSS_SELECTOR, "#listSizeSelectDiv > ul > li:nth-child(7) > a")

## 1. 태그를 보이게 만들고 클릭 실행
driver.find_element(By.CSS_SELECTOR, "#listSizeSelectDiv > a").click()
time.sleep(1)
element.click()

## 2. 자바스크립트를 이용하여 강제로 클릭 실행
# driver.execute_script("arguments[0].click();", element)