from selenium import webdriver
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://naver.com")

# 암시적 대기
driver.implicitly_wait(5)

find_element = driver.find_element(By.CSS_SELECTOR, "#query")
ic(find_element)

# 명시적 대기
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#query"))
)

ic(element)

