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
to_email = os.getenv('to_email')

ic(user_id)
ic(user_pw)
ic(to_email)

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
time.sleep(1)

# 네이버 메인 페이지로 이동
driver.get("https://naver.com")
time.sleep(1)

# 드롭다운 메뉴 클릭 (새로운 창이 열림)
driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(1) > a > span.service_name").click()
time.sleep(1)

# 현재 열려있는 창 리스트
ic(driver.window_handles)

# 새 창으로 전환
driver.switch_to.window(driver.window_handles[1])

# 메일쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(1)

# driver.close()

# 받는 사람 입력
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys(to_email)

# 제목 입력
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys("제목입니다.")

# 내용 iframe 찾기 -> 프레임 전환
iframe = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
driver.switch_to.frame(iframe)

# 내용 입력
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys("내용입니다.")
time.sleep(1)

# 원래 창 선택
driver.switch_to.default_content()

# 보내기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()
time.sleep(1)

# 모든 창 닫기
driver.quit()
