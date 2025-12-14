# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(446, 358)
        self.horizontalLayout_6 = QHBoxLayout(Widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_password = QLineEdit(Widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_4.addWidget(self.lineEdit_password)

        self.checkBox_showPassword = QCheckBox(Widget)
        self.checkBox_showPassword.setObjectName(u"checkBox_showPassword")

        self.horizontalLayout_4.addWidget(self.checkBox_showPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_passwordConfirm = QLineEdit(Widget)
        self.lineEdit_passwordConfirm.setObjectName(u"lineEdit_passwordConfirm")
        self.lineEdit_passwordConfirm.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.lineEdit_passwordConfirm)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_selectInputFile = QPushButton(Widget)
        self.pushButton_selectInputFile.setObjectName(u"pushButton_selectInputFile")

        self.horizontalLayout_2.addWidget(self.pushButton_selectInputFile)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_inputFile = QLineEdit(Widget)
        self.lineEdit_inputFile.setObjectName(u"lineEdit_inputFile")

        self.horizontalLayout_2.addWidget(self.lineEdit_inputFile)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_selectOutputFile = QPushButton(Widget)
        self.pushButton_selectOutputFile.setObjectName(u"pushButton_selectOutputFile")

        self.horizontalLayout.addWidget(self.pushButton_selectOutputFile)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_outputFile = QLineEdit(Widget)
        self.lineEdit_outputFile.setObjectName(u"lineEdit_outputFile")

        self.horizontalLayout.addWidget(self.lineEdit_outputFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_encrypt = QPushButton(Widget)
        self.pushButton_encrypt.setObjectName(u"pushButton_encrypt")

        self.horizontalLayout_3.addWidget(self.pushButton_encrypt)

        self.pushButton_decrypt = QPushButton(Widget)
        self.pushButton_decrypt.setObjectName(u"pushButton_decrypt")

        self.horizontalLayout_3.addWidget(self.pushButton_decrypt)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"File Encryption", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.lineEdit_password.setText("")
        self.checkBox_showPassword.setText(QCoreApplication.translate("Widget", u"Show", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Confirm", None))
        self.pushButton_selectInputFile.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Input file", None))
        self.lineEdit_inputFile.setText("")
        self.pushButton_selectOutputFile.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Output file", None))
        self.lineEdit_outputFile.setText("")
        self.pushButton_encrypt.setText(QCoreApplication.translate("Widget", u"Encrypt", None))
        self.pushButton_decrypt.setText(QCoreApplication.translate("Widget", u"Decrypt", None))
    # retranslateUi

