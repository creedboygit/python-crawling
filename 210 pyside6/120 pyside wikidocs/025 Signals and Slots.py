import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel,
                             QVBoxLayout,
                             QCheckBox, QButtonGroup)
from PyQt6.QtCore import Qt


class MW(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QCheckbox")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()

        lm.addWidget(QLabel('What is most important?'))

        self.bg = QButtonGroup(self)

        self.cb01 = QCheckBox('1. faith')
        lm.addWidget(self.cb01)
        self.bg.addButton(self.cb01)
        self.cb02 = QCheckBox('2. hope')
        lm.addWidget(self.cb02)
        self.bg.addButton(self.cb02)
        self.cb03 = QCheckBox('3. love')
        lm.addWidget(self.cb03)
        self.bg.addButton(self.cb03)

        self.bg.setExclusive(True)
        self.bg.buttonClicked.connect(self.ck_click)

        self.dp_label = QLabel("")
        lm.addWidget(self.dp_label)

        self.cb = QCheckBox('Check it for the multiple selection.')
        # self.cb.toggle()
        self.cb.stateChanged.connect(self.ck_multiple)
        lm.addWidget(self.cb)

        self.setLayout(lm)

    def ck_click(self, button):
        tmp = ""
        tmp = button.text()

        print(tmp)
        self.dp_label.setText(tmp)

    def ck_multiple(self, state):
        if state == Qt.CheckState.Checked:
            self.bg.setExclusive(True)
            for button in self.bg.buttons():
                button.setChecked(False)
        else:
            self.bg.setExclusive(False)
            for button in self.bg.buttons():
                button.setChecked(False)

        # 상태 변경 후 dp_label 업데이트
        self.dp_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
