import os
import time
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

user_id = os.getenv('user_id')
user_pw = os.getenv('user_pw')

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(1)
wait = WebDriverWait(driver, 10)

def input_text_via_clipboard(element, text):
    pyperclip.copy(text)
    element.click()
    time.sleep(1)
    if platform.system() == 'Darwin':  # macOS
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    else:  # Windows or Linux
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

id_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id")))
input_text_via_clipboard(id_field, user_id)
time.sleep(1)
pw_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pw")))
input_text_via_clipboard(pw_field, user_pw)
time.sleep(1)
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#log\\.login")))
login_button.click()

# 캡차가 나타날 경우 사용자 입력을 기다립니다
input("캡차가 나타나면 직접 입력한 후 Enter를 눌러주세요...")

# 로그인 성공 여부 확인
try:
    wait.until(EC.url_contains("https://www.naver.com/"))
    print("로그인 성공!")
except:
    print("로그인 실패. 수동으로 확인해주세요.")

# 브라우저를 열린 상태로 유지
input("Press Enter to close the browser...")
driver.quit()