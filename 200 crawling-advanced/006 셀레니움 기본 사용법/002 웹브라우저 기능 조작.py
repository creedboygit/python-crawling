from selenium import webdriver
from icecream import ic

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 원하는 페이지로 이동
driver.get("https://www.naver.com")

# 뒤로가기
driver.back()

# 앞으로 가기
driver.forward()

# 새로고침
driver.refresh()

# 현재 URL 확인
url = driver.current_url
ic(url)

# 페이지 타이틀 확인
title = driver.title
ic(title)

# 최대화
driver.maximize_window()

# 최소화
driver.minimize_window()

# 현재 창 닫기
driver.close()

# 모든 창을 닫고, 웹드라이버 세션 종료
driver.quit()
