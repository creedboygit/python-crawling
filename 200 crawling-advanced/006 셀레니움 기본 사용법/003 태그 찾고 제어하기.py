from selenium import webdriver
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://www.naver.com")

# 태그 찾기
# element = driver.find_element(By.CSS_SELECTOR, "#query")
search = driver.find_element(By.ID, "query")
ic(search)

# 클릭
search.click()

# 검색어 입력
search.send_keys("카즈하")

# 키 입력
search.send_keys(Keys.ENTER)