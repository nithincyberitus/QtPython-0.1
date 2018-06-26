# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showTime.ui',
# licensing of 'showTime.ui' applies.
#
# Created: Fri Jun 22 13:19:24 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528453888
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_showTime(object):
    def setupUi(self, Form_showTime):
        Form_showTime.setObjectName("Form_showTime")
        Form_showTime.resize(400, 300)
        self.Button_showTime = QtWidgets.QPushButton(Form_showTime)
        self.Button_showTime.setGeometry(QtCore.QRect(76, 140, 241, 27))
        self.Button_showTime.setObjectName("Button_showTime")
        self.label_showTime = QtWidgets.QLabel(Form_showTime)
        self.label_showTime.setGeometry(QtCore.QRect(85, 50, 231, 61))
        self.label_showTime.setText("")
        self.label_showTime.setObjectName("label_showTime")

        self.retranslateUi(Form_showTime)
        QtCore.QMetaObject.connectSlotsByName(Form_showTime)

    def retranslateUi(self, Form_showTime):
        Form_showTime.setWindowTitle(QtWidgets.QApplication.translate("Form_showTime", "Form", None, -1))
        self.Button_showTime.setText(QtWidgets.QApplication.translate("Form_showTime", "Show Time", None, -1))

