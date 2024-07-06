import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_login import Ui_Dialog


class MainWindow(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.객체이름.clicked.connect(self.실행할메서드이름)
        self.login_btn.clicked.connect(self.login)

    def login(self):
        print(f"아이디: {self.id.text()} / 비밀번호: {self.pw.text()}")


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
