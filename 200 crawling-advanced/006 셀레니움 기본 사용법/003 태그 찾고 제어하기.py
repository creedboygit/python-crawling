from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://www.naver.com")

# 태그 찾기
from selenium.webdriver.common.by import By

# element = driver.find_element(By.CSS_SELECTOR, "#query")
element = driver.find_element(By.ID, "query")
element.send_keys("카즈하")


