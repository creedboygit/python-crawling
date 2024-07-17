import json
import os
import platform
import time
from getpass import getpass

from pwinput import pwinput
import pyperclip
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# user_id = os.getenv('user_id')
# user_pw = os.getenv('user_pw')

# user_id = input("아이디를 입력해 주세요: ")
# user_pw = input("비밀번호를 입력해 주세요: ")
# user_pw = pwinput("비밀번호를 입력해 주세요: ", mask="*")

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
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
    return driver


def input_text_via_clipboard(driver, element, text):
    pyperclip.copy(text)
    element.click()
    time.sleep(1)
    if platform.system() == 'Darwin':  # macOS
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    else:  # Windows or Linux
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


def login_to_naver(driver):
    driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://mail.naver.com/")
    time.sleep(1)
    wait = WebDriverWait(driver, 10)

    # id_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id")))
    # input_text_via_clipboard(driver, id_field, user_id)
    #
    # pw_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pw")))
    # input_text_via_clipboard(driver, pw_field, user_pw)
    #
    # login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#log\\.login")))
    # login_button.click()
    time.sleep(1)

    # input("캡차가 나타나면 직접 입력한 후 Enter를 눌러주세요...")

    try:
        wait.until(EC.url_contains("https://mail.naver.com/"))
        print("로그인 성공!")
        time.sleep(2)
        return True
    except:
        print("로그인 실패. 수동으로 확인해주세요.")
        return False


def get_email_list(session):
    url = "https://mail.naver.com/json/list?folderSN=-1&startOffset=1&pageSize4SeeMore=100&viewMode=time&previewMode=2&sortField=1&sortType=0&u="
    response = session.post(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        emails = []

        for item in data.get('mailData', []):
            email = {
                'subject': item.get('subject', ''),
                'sender': item.get('from', {}).get('name', ''),
                'date': item.get('receivedTime', ''),
                'volume': item.get('size', '')
            }
            emails.append(email)

        return emails
    else:
        print(f"이메일 목록을 가져오는데 실패했습니다. 상태 코드: {response.status_code}")
        return []


def main():
    driver = setup_driver()
    if login_to_naver(driver):
        cookies = driver.get_cookies()
        driver.quit()

        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])

        emails = get_email_list(session)
        print(f"총 {len(emails)}개의 이메일을 가져왔습니다.")
        for email in emails:
            print(f"제목: {email['subject']}")
            print(f"보낸사람: {email['sender']}")
            print(f"날짜: {email['date']}")
            print(f"용량: {email['volume']}")
            print("-" * 50)
    else:
        print("로그인에 실패했습니다.")


if __name__ == "__main__":
    main()