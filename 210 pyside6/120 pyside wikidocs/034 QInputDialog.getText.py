import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QPushButton, QLabel, QVBoxLayout,
    QLineEdit, QInputDialog)


class MW(QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):

        self.button0 = QPushButton('Test.')
        self.button0.clicked.connect(self.slot00)

        self.ret_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.button0)
        layout.addWidget(self.ret_label)

        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        print(self.sender())

        sender = self.sender()

        if sender == self.button0:
            ret_text, is_ok = QInputDialog.getText(
                self,
                "Input Text",
                "Enter Your Text!",
                # QLineEdit.EchoMode.PasswordEchoOnEdit,
                # QLineEdit.EchoMode.Normal,
                # QLineEdit.EchoMode.Password,
                QLineEdit.EchoMode.NoEcho,
                "default text!",
            )
            if is_ok:
                self.ret_label.setText(f'{ret_text}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())
