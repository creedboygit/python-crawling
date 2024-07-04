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
# ic(product_name)

items = soup.select(".product")
for item in items:
    category = item.select_one(".product-category").text
    name = item.select_one(".product-name").text
    link = item.select_one(".product-name > a").attrs["href"]
    price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
    ic(category, name, link, price)