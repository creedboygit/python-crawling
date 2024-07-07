import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_naver_kin import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
