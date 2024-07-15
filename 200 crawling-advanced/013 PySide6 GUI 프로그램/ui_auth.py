# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authDYlRan.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(429, 216)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 30, 81, 31))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.auth_key_input = QLineEdit(Form)
        self.auth_key_input.setObjectName(u"lineEdit")
        self.auth_key_input.setGeometry(QRect(90, 70, 221, 31))
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(110, 120, 191, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.login_btn.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc778\uc99d\ud0a4", None))
        self.auth_key_input.setPlaceholderText(QCoreApplication.translate("Form", u"\uc778\uc99d\ud0a4\ub97c \uc785\ub825\ud574 \uc8fc\uc138\uc694.", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\uc778\uc99d", None))
    # retranslateUi

