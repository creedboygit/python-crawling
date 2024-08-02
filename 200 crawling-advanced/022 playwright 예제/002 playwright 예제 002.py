from playwright.sync_api import sync_playwright


def run(playwright):
    # 브라우저 실행
    browser = playwright.chromium.launch(headless=True)
    # 새로운 페이지 열기
    page = browser.new_page()
    # 특정 URL로 이동
    page.goto('https://naver.com')
    # 페이지 제목 출력
    print(page.title())
    # 페이지 스크린샷 찍기
    page.screenshot(path='naver.png')
    # 브라우저 종료
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
