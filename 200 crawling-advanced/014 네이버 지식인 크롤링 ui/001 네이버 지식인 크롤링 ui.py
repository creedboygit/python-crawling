import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_naver_kin import Ui_Form
import requests
from bs4 import BeautifulSoup
from icecream import ic

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.객체이름.clicked.connect(self.실행할메서드이름)
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.quit_btn.clicked.connect(self.quit)

    def start(self):
        # print(f"시작버튼클릭됨")
        input_keyword = self.keyword.text()
        input_page = int(self.page.text())

        for i in range(1, input_page + 1):
            ## 로그
            self.textBrowser.append(f"{i} 페이지 크롤링 중...")

            response = requests.get(f'https://kin.naver.com/search/list.naver?query={input_keyword}&page={i}')
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            posts = soup.select(".basic1 > li")
            for post in posts:
                title = post.select_one("._nclicks\\:kin\\.txt").text
                link = post.select_one("._nclicks\\:kin\\.txt").attrs['href']
                date = post.select_one(".txt_inline").text
                category = post.select_one(".txt_block > a:nth-of-type(2)").text
                review = post.select_one(".txt_block > span:nth-of-type(2)").text.split("답변수")[1].strip()

                ## 로그
                self.textBrowser.append(title)

                ic(title, link, date, category, review)

        ## 로그
        self.textBrowser.append("크롤링 완료!")

    def reset(self):
        print(f"리셋버튼클릭됨")

    def save(self):
        print(f"저장버튼클릭됨")

    def quit(self):
        print(f"종료버튼클릭됨")


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
