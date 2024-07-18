# ---------------------------------
# PyQt6 용 module
import sys
import PyQt6.QtCore
from PyQt6.QtWidgets import (QApplication, QWidget,
                               QLabel)
# ---------------------------------
# PySide6 용 module
# import PySide6.QtCore
# from PySide6.QtWidgets import (QApplication, QWidget,
#                                QLabel)

# ================================
# define classes for this program

class MW(QWidget):
    def __init__(self):
        """ Constructor for Main Window Class """
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """setup GUI application."""
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PyQt")
        self.setup_main_wnd()
        self.show() # Display the window on the screen

    def setup_main_wnd(self):
        """set up the main window."""
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!')
        hello_label.move(150,90)

# ===============================
# Run the program
if __name__ == '__main__':
    # -----------------------------
    # PySide6 관련 부분.
    # print(PySide6.__version__)
    # print(PySide6.QtCore.__version__)

    # -----------------------------
    # PyQt6 관련 부분.
    print(PyQt6.QtCore.qVersion()) # PyQt6 버전 check.

    # Event Loop 등을 위한 QApplication instance 생성.
    app = QApplication(sys.argv)
    # main window 생성 및 show 호출.
    window = MW()
    # Event Loop 시작.
    sys.exit(app.exec())