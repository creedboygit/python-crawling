import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QFileDialog,
)
from PySide6.QtGui import (
    QTextCursor,
    QTextCharFormat,
    QFont,
)


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout(self)

        # 텍스트 에디터 위젯 생성
        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        # 볼드 버튼
        btn_bold = QPushButton('Bold', self)
        btn_bold.clicked.connect(self.make_bold)
        layout.addWidget(btn_bold)

        # 이탤릭 버튼
        btn_italic = QPushButton('Italic', self)
        btn_italic.clicked.connect(self.make_italic)
        layout.addWidget(btn_italic)

        # 텍스트 저장 버튼
        btn_save = QPushButton('Save Text', self)
        btn_save.clicked.connect(self.save_text)
        layout.addWidget(btn_save)

        tmp = QWidget()
        tmp.setLayout(layout)
        self.setCentralWidget(tmp)

    def make_bold(self):
        # 선택된 텍스트를 볼드로 설정
        cursor = self.textEdit.textCursor()
        format = QTextCharFormat()
        format.setFontWeight(QFont.Bold)
        cursor.mergeCharFormat(format)

    def make_italic(self):
        # 선택된 텍스트를 이탤릭으로 설정
        cursor = self.textEdit.textCursor()  # cursor 객체를 얻어옴.
        format = QTextCharFormat()
        format.setFontItalic(True)
        cursor.mergeCharFormat(format)  # 현재 커서위치 또는 선택된 영역의 character format을 재설정.

    def save_text(self):
        # 텍스트를 파일로 저장
        filename, _ = QFileDialog.getSaveFileName(self, "Save File")
        if filename:
            with open(filename, 'w') as file:
                file.write(self.textEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())
