# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showDateTime.ui',
# licensing of 'showDateTime.ui' applies.
#
# Created: Thu Jun 21 16:18:49 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528453888
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ShowDateTime(object):
    def setupUi(self, ShowDateTime):
        ShowDateTime.setObjectName("ShowDateTime")
        ShowDateTime.resize(400, 300)
        self.show_Date = QtWidgets.QLabel(ShowDateTime)
        self.show_Date.setGeometry(QtCore.QRect(70, 10, 81, 41))
        self.show_Date.setText("")
        self.show_Date.setObjectName("show_Date")
        self.ShowDate = QtWidgets.QPushButton(ShowDateTime)
        self.ShowDate.setGeometry(QtCore.QRect(60, 100, 97, 27))
        self.ShowDate.setObjectName("ShowDate")
        self.showTime = QtWidgets.QPushButton(ShowDateTime)
        self.showTime.setGeometry(QtCore.QRect(240, 100, 97, 27))
        self.showTime.setObjectName("showTime")
        self.show_Time = QtWidgets.QLabel(ShowDateTime)
        self.show_Time.setGeometry(QtCore.QRect(240, 0, 81, 41))
        self.show_Time.setText("")
        self.show_Time.setObjectName("show_Time")
        self.show_date_time = QtWidgets.QLabel(ShowDateTime)
        self.show_date_time.setGeometry(QtCore.QRect(105, 150, 181, 41))
        self.show_date_time.setText("")
        self.show_date_time.setObjectName("show_date_time")
        self.show_Date_Time = QtWidgets.QPushButton(ShowDateTime)
        self.show_Date_Time.setGeometry(QtCore.QRect(150, 220, 97, 27))
        self.show_Date_Time.setObjectName("show_Date_Time")

        self.retranslateUi(ShowDateTime)
        QtCore.QMetaObject.connectSlotsByName(ShowDateTime)

    def retranslateUi(self, ShowDateTime):
        ShowDateTime.setWindowTitle(QtWidgets.QApplication.translate("ShowDateTime", "Dialog", None, -1))
        self.ShowDate.setText(QtWidgets.QApplication.translate("ShowDateTime", "Show Date", None, -1))
        self.showTime.setText(QtWidgets.QApplication.translate("ShowDateTime", "Show Time", None, -1))
        self.show_Date_Time.setText(QtWidgets.QApplication.translate("ShowDateTime", "Show Date Time", None, -1))

