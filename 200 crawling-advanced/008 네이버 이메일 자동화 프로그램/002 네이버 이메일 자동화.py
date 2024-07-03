import os
import sys

from selenium import webdriver
from icecream import ic
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pyperclip

# user_id = "아이디"
# user_pw = "비밀번호"

user_id = os.getenv('user_id')
user_pw = os.getenv('user_pw')

ic(user_id)
ic(user_pw)

# ChromeOptions 객체 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

# 페이지 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(1)

# 아이디 입력
# 아이디 복사
pyperclip.copy(user_id)

id = driver.find_element(By.CSS_SELECTOR, "#id")
id.send_keys(Keys.CONTROL, 'v')
# id.send_keys(user_id)
time.sleep(1)

# 비밀번호 입력
pyperclip.copy(user_pw)
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.send_keys(Keys.CONTROL, 'v')
# pw.send_keys(user_pw)
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#log\\.login").click()

# 네이버 메인 페이지로 이동
driver.get("https://naver.com")

time.sleep(1)

# 드롭다운 메뉴 클릭
driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(1) > a > span.service_name").click()

