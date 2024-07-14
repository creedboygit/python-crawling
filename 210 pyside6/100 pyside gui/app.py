import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from login_ui import Ui_MainWindow

class Login_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login_Window, self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)

window = Login_Window()
window.show()

app.exec()