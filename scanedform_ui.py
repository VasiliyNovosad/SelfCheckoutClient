# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanedForm.ui'
#
# Created: Fri Mar 03 03:50:03 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        Dialog.setMinimumSize(QtCore.QSize(600, 500))
        Dialog.setMaximumSize(QtCore.QSize(600, 500))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 450))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonsStackedWidget = QtGui.QStackedWidget(self.frame)
        self.buttonsStackedWidget.setMinimumSize(QtCore.QSize(0, 59))
        self.buttonsStackedWidget.setMaximumSize(QtCore.QSize(16777215, 59))
        self.buttonsStackedWidget.setObjectName("buttonsStackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verifyPushButton = QtGui.QPushButton(self.page)
        self.verifyPushButton.setGeometry(QtCore.QRect(0, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.verifyPushButton.setFont(font)
        self.verifyPushButton.setObjectName("verifyPushButton")
        self.cancelPushButton = QtGui.QPushButton(self.page)
        self.cancelPushButton.setGeometry(QtCore.QRect(394, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.buttonsStackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.verifyPushButton2 = QtGui.QPushButton(self.page_2)
        self.verifyPushButton2.setGeometry(QtCore.QRect(0, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.verifyPushButton2.setFont(font)
        self.verifyPushButton2.setObjectName("verifyPushButton2")
        self.cancelPushButton2 = QtGui.QPushButton(self.page_2)
        self.cancelPushButton2.setGeometry(QtCore.QRect(394, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancelPushButton2.setFont(font)
        self.cancelPushButton2.setObjectName("cancelPushButton2")
        self.buttonsStackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.cancelPushButton3 = QtGui.QPushButton(self.page_3)
        self.cancelPushButton3.setGeometry(QtCore.QRect(4, 10, 553, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancelPushButton3.setFont(font)
        self.cancelPushButton3.setObjectName("cancelPushButton3")
        self.buttonsStackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.buttonsStackedWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scanedGoodImageLabel = QtGui.QLabel(self.frame)
        self.scanedGoodImageLabel.setMinimumSize(QtCore.QSize(600, 300))
        self.scanedGoodImageLabel.setMaximumSize(QtCore.QSize(600, 300))
        self.scanedGoodImageLabel.setBaseSize(QtCore.QSize(600, 300))
        self.scanedGoodImageLabel.setText("")
        self.scanedGoodImageLabel.setPixmap(QtGui.QPixmap("images/9402-bananas.jpg"))
        self.scanedGoodImageLabel.setScaledContents(False)
        self.scanedGoodImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scanedGoodImageLabel.setObjectName("scanedGoodImageLabel")
        self.verticalLayout_4.addWidget(self.scanedGoodImageLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scanedGoodNameLabel = QtGui.QLabel(self.frame)
        self.scanedGoodNameLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.scanedGoodNameLabel.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.scanedGoodNameLabel.setFont(font)
        self.scanedGoodNameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.scanedGoodNameLabel.setObjectName("scanedGoodNameLabel")
        self.horizontalLayout_3.addWidget(self.scanedGoodNameLabel)
        self.scanedGoodPriceLabel = QtGui.QLabel(self.frame)
        self.scanedGoodPriceLabel.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.scanedGoodPriceLabel.setFont(font)
        self.scanedGoodPriceLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.scanedGoodPriceLabel.setObjectName("scanedGoodPriceLabel")
        self.horizontalLayout_3.addWidget(self.scanedGoodPriceLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scanedGoodDescriptionLabel = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scanedGoodDescriptionLabel.setFont(font)
        self.scanedGoodDescriptionLabel.setWordWrap(True)
        self.scanedGoodDescriptionLabel.setObjectName("scanedGoodDescriptionLabel")
        self.horizontalLayout_2.addWidget(self.scanedGoodDescriptionLabel)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.scanedGoodExpirationLabel = QtGui.QLabel(self.frame)
        self.scanedGoodExpirationLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.scanedGoodExpirationLabel.setFont(font)
        self.scanedGoodExpirationLabel.setWordWrap(True)
        self.scanedGoodExpirationLabel.setObjectName("scanedGoodExpirationLabel")
        self.horizontalLayout_2.addWidget(self.scanedGoodExpirationLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.buttonsStackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.verifyPushButton.setText(QtGui.QApplication.translate("Dialog", "Put into Cart to Verify", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelPushButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.verifyPushButton2.setText(QtGui.QApplication.translate("Dialog", "Not Verified, Try Once", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelPushButton2.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelPushButton3.setText(QtGui.QApplication.translate("Dialog", "Verified", None, QtGui.QApplication.UnicodeUTF8))
        self.scanedGoodNameLabel.setText(QtGui.QApplication.translate("Dialog", "Coca-cola 0.5L", None, QtGui.QApplication.UnicodeUTF8))
        self.scanedGoodPriceLabel.setText(QtGui.QApplication.translate("Dialog", "1.99€", None, QtGui.QApplication.UnicodeUTF8))
        self.scanedGoodDescriptionLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.scanedGoodExpirationLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

