import sys

import requests
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_auth import Ui_Form
from ui_login import Ui_Dialog
from icecream import ic


class AuthWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.authenticate)
        self.auth_key_input.returnPressed.connect(self.login_btn.click)
        self.auth_key = "1234"  # 실제 사용 시 보안을 위해 이 부분을 적절히 수정해야 합니다

    def authenticate(self):
        scrom_auth_result = self.scrom_auth(self.auth_key_input.text())
        # if self.lineEdit.text() == self.auth_key:
        if (scrom_auth_result['status'] == 'success'):
            self.login_window = LoginWindow()
            self.login_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "인증 실패", "잘못된 인증키입니다.")
            self.auth_key_input.clear()
            self.auth_key_input.setFocus()

    def scrom_auth(self, auth_key):
        response = requests.get(f"http://scrom.co.kr/test/20240712_authapi_test/test.html?auth_key={auth_key}")
        json = response.json()
        ic(json)
        return json



class LoginWindow(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id.setFocus()
        self.login_btn.clicked.connect(self.login)
        self.id.returnPressed.connect(self.pw.setFocus)
        self.pw.returnPressed.connect(self.login)

    def login(self):
        print(f"아이디: {self.id.text()} / 비밀번호: {self.pw.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    auth_window = AuthWindow()
    auth_window.show()

    sys.exit(app.exec())