import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QLabel, QTextEdit,
    QVBoxLayout, QWidget, QFileDialog, QMenuBar,
    QStatusBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction


class TextDisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout()

        # Label for plain text
        labelPlainText = QLabel("Using setPlainText:")
        layout.addWidget(labelPlainText)

        # QTextEdit for plain text
        self.textEditPlainText = QTextEdit()
        self.textEditPlainText.setPlainText(
            "This is a sample <b>bold</b> text with <i>italics</i> and a <a href='https://example.com'>link</a>.")
        layout.addWidget(self.textEditPlainText)

        # Label for HTML
        labelHTML = QLabel("Using setHtml:")
        layout.addWidget(labelHTML)

        # QTextEdit for HTML
        self.textEditHtml = QTextEdit()
        self.textEditHtml.setHtml(
            "This is a sample <b>bold</b> text with <i>italics</i> and a <a href='https://example.com'>link</a>.")
        layout.addWidget(self.textEditHtml)

        centralWidget.setLayout(layout)
        self.setWindowTitle('setPlainText vs setHtml Example')
        self.setGeometry(300, 300, 400, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = TextDisplayWindow()
    mainWindow.show()
    sys.exit(app.exec())
