# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 379)
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(112, 220, 301, 51))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.login_btn.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 37, 131, 61))
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 120, 131, 61))
        self.label_2.setFont(font)
        self.id = QLineEdit(Dialog)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(160, 60, 251, 51))
        self.pw = QLineEdit(Dialog)
        self.pw.setObjectName(u"pw")
        self.pw.setGeometry(QRect(160, 140, 251, 51))
        self.pw.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"\ub85c\uadf8\uc778", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\uc544\uc774\ub514", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\ube44\ubc00\ubc88\ud638", None))
        self.pw.setPlaceholderText(QCoreApplication.translate("Dialog", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
    # retranslateUi

