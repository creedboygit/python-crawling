import sys
import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from openpyxl import Workbook


class NaverSearchUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naver Search Results to Excel")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.search_label = QLabel("검색어:")
        layout.addWidget(self.search_label)

        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("검색")
        self.search_button.clicked.connect(self.search_naver)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    def search_naver(self):
        query = self.search_input.text()
        if query:
            url = f"https://search.naver.com/search.naver?query={query}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            titles = [title.text for title in soup.select(".bx._svp_item .total_tit")]

            if titles:
                wb = Workbook()
                ws = wb.active
                ws.append(["검색 결과 제목"])
                for title in titles:
                    ws.append([title])

                wb.save(f"{query}_results.xlsx")
                QMessageBox.information(self, "저장 완료", f"{query}_results.xlsx 파일로 저장되었습니다.")
            else:
                QMessageBox.warning(self, "검색 결과 없음", "검색 결과가 없습니다.")
        else:
            QMessageBox.warning(self, "검색어 없음", "검색어를 입력해주세요.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = NaverSearchUI()
    ui.show()
    sys.exit(app.exec())