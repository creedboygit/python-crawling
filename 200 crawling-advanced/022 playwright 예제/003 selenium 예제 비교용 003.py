from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드 설정
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Chrome 드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 특정 URL로 이동
    driver.get('https://naver.com')

    # 페이지 제목 출력
    print(driver.title)

    # 페이지 스크린샷 찍기
    driver.save_screenshot('naver2.png')
finally:
    # 브라우저 종료
    driver.quit()
