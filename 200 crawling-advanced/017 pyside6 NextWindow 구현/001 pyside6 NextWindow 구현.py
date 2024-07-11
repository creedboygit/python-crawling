import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class KeyInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Input")
        self.secret_key = "1234"  # 정답 키

        layout = QVBoxLayout()
        self.label = QLabel("Enter the secret key:")
        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.check_key)  # 엔터 키 이벤트 연결
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_key)

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_key(self):
        entered_key = self.input_field.text()
        if entered_key == self.secret_key:
            self.close()
            self.next_window = NextWindow()
            self.next_window.show()
        else:
            self.label.setText("Wrong key. Try again.")
            self.input_field.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.check_key()
        else:
            super().keyPressEvent(event)

class NextWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Next Window")

        layout = QVBoxLayout()
        self.label = QLabel("Welcome to the next window!")
        layout.addWidget(self.label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyInputWindow()
    window.show()
    sys.exit(app.exec())