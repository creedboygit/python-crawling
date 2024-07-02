from selenium import webdriver
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://startcoding.pythonanywhere.com/basic")

# 태그 찾기
labels = driver.find_elements(By.CSS_SELECTOR, "label[for]")
ic(labels)

for label in labels:
    label.click()
    time.sleep(0.2)

for label in labels:
    ic(label.text, label.get_attribute('for'))