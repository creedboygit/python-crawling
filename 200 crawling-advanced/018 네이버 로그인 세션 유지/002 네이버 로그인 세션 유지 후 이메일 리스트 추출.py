from icecream import ic
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
import requests
from bs4 import BeautifulSoup

user_id = os.getenv('user_id')
user_pw = os.getenv('user_pw')


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

    id_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id")))
    input_text_via_clipboard(driver, id_field, user_id)

    pw_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pw")))
    input_text_via_clipboard(driver, pw_field, user_pw)

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#log\\.login")))
    login_button.click()
    time.sleep(1)

    input("캡차가 나타나면 직접 입력한 후 Enter를 눌러주세요...")

    try:
        wait.until(EC.url_contains("https://mail.naver.com/"))
        print("로그인 성공!")
        time.sleep(2)
        return True
    except:
        print("로그인 실패. 수동으로 확인해주세요.")
        return False


def get_naver_cookies(driver):
    return driver.get_cookies()


def verify_login(session):
    response = session.get('https://mail.naver.com/')
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 로그인 상태 확인
    if "로그아웃" in response.text:
        print("로그인 상태가 유지되고 있습니다.")
        return True
    else:
        print("로그인 상태가 유지되지 않고 있습니다.")
        return False


def get_email_list(session):
    # response = session.get('https://mail.naver.com/')

    print(session.headers)
    print(session.cookies)
    headers2 = {
        "host": "mail.naver.com",
        "connection": "keep-alive",
        "content-length": "0",
        "sec-ch-ua": '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="124"',
        "accept": "application/json, text/plain, */*",
        "charset": "utf-8",
        "cache-control": "no-cache",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Whale/3.26.244.21 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "origin": "https://mail.naver.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://mail.naver.com/v2/folders/-1",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    session.headers.update(headers2)
    # session.cookies.update(cookie_dict)
    ic(session.cookies)


    response = session.post('https://mail.naver.com/json/list?folderSN=-1&startOffset=1&pageSize4SeeMore=100&viewMode=time&previewMode=2&sortField=1&sortType=0&u=')
    # response = session.post('https://mail.naver.com/json/list?folderSN=-1&startOffset=1&pageSize4SeeMore=100&viewMode=time&previewMode=2&sortField=1&sortType=0&u=holdens', headers=headers2)
    ic(response)

    ic(response.json())

    soup = BeautifulSoup(response.text, 'html.parser')

    # 디버깅: HTML 내용 출력
    print("HTML 내용:")
    print(response.text[:1000])  # 처음 1000자만 출력

    emails = []
    email_list = soup.select('.mail_item')
    print(f"찾은 이메일 항목 수: {len(email_list)}")

    for email in email_list:
        try:
            subject = email.select_one('.mail_title_link .text').text.strip()
            sender = email.select_one('.button_sender').text.strip()
            date = email.select_one('.mail_date').text.strip()
            volume = email.select_one('.mail_volume').text.strip()
            emails.append({
                'subject': subject,
                'sender': sender,
                'date': date,
                'volume': volume
            })
        except Exception as e:
            print(f"Error extracting email info: {e}")

    return emails


def main():
    driver = setup_driver()
    if login_to_naver(driver):
        cookies = get_naver_cookies(driver)

        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']

        driver.quit()

        session = requests.Session()

        headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

        session.headers.update(headers)
        session.cookies.update(cookie_dict)

        print(session.headers)
        print(session.cookies)

        # for cookie in cookies:
        #     c = {cookie['name']: cookie['value']}
        #
        #     session.cookies.update(c)
        #     session.cookies.set(cookie['name'], cookie['value'])

        # print(session.cookies)

        # if verify_login(session):
        emails = get_email_list(session)
        print(f"총 {len(emails)}개의 이메일을 가져왔습니다.")
        for email in emails:
            print(f"제목: {email['subject']}")
            print(f"보낸사람: {email['sender']}")
            print(f"날짜: {email['date']}")
            print(f"용량: {email['volume']}")
            print("-" * 50)
        # else:
        #     print("로그인 세션이 유지되지 않아 이메일을 가져올 수 없습니다.")
    else:
        print("로그인에 실패했습니다.")


if __name__ == "__main__":
    main()