# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combine.ui',
# licensing of 'combine.ui' applies.
#
# Created: Thu Jun 21 15:25:38 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528453888
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow_CCPL = QtWidgets.QAction(MainWindow)
        self.actionShow_CCPL.setObjectName("actionShow_CCPL")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setCheckable(False)
        self.action_Close.setObjectName("action_Close")
        self.menu_File.addAction(self.actionShow_CCPL)
        self.menu_File.addAction(self.action_About)
        self.menu_File.addAction(self.action_Close)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Close, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.actionShow_CCPL.setText(QtWidgets.QApplication.translate("MainWindow", "Show &CCPL", None, -1))
        self.action_About.setText(QtWidgets.QApplication.translate("MainWindow", "&About", None, -1))
        self.action_Close.setText(QtWidgets.QApplication.translate("MainWindow", "Close   &X", None, -1))

