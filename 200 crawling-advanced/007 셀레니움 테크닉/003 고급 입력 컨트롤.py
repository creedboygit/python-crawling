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

# 태그 찾기
search = driver.find_element(By.CSS_SELECTOR, "#query")

# 클릭
search.click()

# 문자 입력
search.send_keys("카즈하")

# 입력값 삭제
# time.sleep(3)
# search.clear()

# 순차적 키 입력
search.send_keys(Keys.CONTROL, 'a')