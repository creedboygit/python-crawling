from selenium import webdriver
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://finance.naver.com/research/company_list.naver")

# select 태그 찾기
select_tag = driver.find_element(By.CSS_SELECTOR, "#contentarea_left > form > fieldset > ul > li:nth-child(2) > select")
ic(select_tag)

select_tag = driver.find_elements(By.XPATH, '//*[@id="contentarea_left"]/form/fieldset/ul/li[2]/select')
ic(select_tag)

# index로 선택
Select(select_tag[0]).select_by_index(2)