from selenium import webdriver
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://naver.com")

# 암시적 대기
# 5초 동안 무조건 대기
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "#query1")
