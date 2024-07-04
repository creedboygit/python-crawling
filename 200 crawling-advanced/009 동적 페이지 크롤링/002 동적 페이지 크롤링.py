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

source = driver.page_source
# ic(source)

soup = BeautifulSoup(source, "lxml")
# ic(soup)

product_name = soup.select_one(".product-name").text
ic(product_name)
