# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_naver_kinkzyRvV.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(540, 682)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Malgun Gothic"])
        font.setPointSize(19)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.keyword = QLineEdit(Form)
        self.keyword.setObjectName(u"keyword")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyword.sizePolicy().hasHeightForWidth())
        self.keyword.setSizePolicy(sizePolicy)
        self.keyword.setMinimumSize(QSize(0, 0))
        self.keyword.setMaximumSize(QSize(16777215, 16777215))
        self.keyword.setSizeIncrement(QSize(50, 0))
        self.keyword.setBaseSize(QSize(53, 0))
        font2 = QFont()
        font2.setFamilies([u"Malgun Gothic"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.keyword.setFont(font2)
        self.keyword.setMaxLength(32783)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.keyword)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.page = QLineEdit(Form)
        self.page.setObjectName(u"page")
        self.page.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.page)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.textBrowser.setFont(font3)

        self.horizontalLayout.addWidget(self.textBrowser)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_btn = QPushButton(Form)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setFont(font1)

        self.verticalLayout.addWidget(self.start_btn)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setFont(font1)

        self.verticalLayout.addWidget(self.reset_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setFont(font1)

        self.verticalLayout.addWidget(self.save_btn)

        self.quit_btn = QPushButton(Form)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setFont(font1)

        self.verticalLayout.addWidget(self.quit_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#02cb1c;\">\ub124\uc774\ubc84 \uc9c0\uc2dd\uc778 \ud06c\ub864\ub9c1</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"\ud0a4\uc6cc\ub4dc", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ud398\uc774\uc9c0\uc218", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\ucd94\ucd9c\uc2dc\uc791", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\ub9ac\uc14b", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5", None))
        self.quit_btn.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
    # retranslateUi

