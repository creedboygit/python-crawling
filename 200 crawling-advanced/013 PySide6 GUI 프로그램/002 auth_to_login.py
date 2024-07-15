import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_auth import Ui_Form
from ui_login import Ui_Dialog


class AuthWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.authenticate)
        self.lineEdit.returnPressed.connect(self.login_btn.click)
        self.auth_key = "1234"  # 실제 사용 시 보안을 위해 이 부분을 적절히 수정해야 합니다

    def authenticate(self):
        if self.lineEdit.text() == self.auth_key:
            self.login_window = LoginWindow()
            self.login_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "인증 실패", "잘못된 인증키입니다.")


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