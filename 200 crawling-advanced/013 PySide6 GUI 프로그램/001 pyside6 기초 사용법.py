import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_login import Ui_Dialog


class MainWindow(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
