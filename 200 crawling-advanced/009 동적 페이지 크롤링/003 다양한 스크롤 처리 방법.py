import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from icecream import ic

# ChromeOptions 객체 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

# 페이지 이동
driver.get("https://startcoding.pythonanywhere.com/dynamic")

# 절대 위치로 스크롤
# driver.execute_script("window.scrollTo(0, 3000);")

# 상대 위치로 스크롤
# driver.execute_script("window.scrollBy(0, 3000);")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 3000);")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 3000);")

# 현재 스크롤 높이 구하기
# scroll_height = driver.execute_script("return document.body.scrollHeight;")
# ic(scroll_height)

# 페이지 끝까지 스크롤하기
scroll_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
ic(scroll_height)

time.sleep(1)

scroll_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
ic(scroll_height)

time.sleep(1)

scroll_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
ic(scroll_height)

time.sleep(1)

scroll_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
ic(scroll_height)