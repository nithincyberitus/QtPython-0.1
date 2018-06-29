import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        Main_Layout = Main_Widget()
        self.setCentralWidget(Main_Layout)

class Main_Widget(QWidget):
    def __init__(self):
        super(Main_Widget,self).__init__()

        First = First_Widget()
        Second = Second_Widget()
        Third = Second_Widget()
        Line = QFrame()
        Line.setFrameShape(QFrame.VLine)
        Line.setFrameShadow(QFrame.Sunken)
        H_Layout = QHBoxLayout()
        H_Layout.addWidget(Second)
        #H_Layout.addWidget(First)
        H_Layout.addWidget(Line)
        H_Layout.addWidget(Third)
        self.setLayout(H_Layout)

class First_Widget(QWidget):
    def __init__(self):
        super(First_Widget,self).__init__()
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        V_layout = QVBoxLayout()
        V_layout.addWidget(button1)
        V_layout.addWidget(button2)
        self.setLayout(V_layout)

class Second_Widget(QWidget):
    def __init__(self):
        super(Second_Widget,self).__init__()
        label_Username = QLabel("User Name")
        label_Password = QLabel("Password")
        txt_UserName = QLineEdit()
        txt_Password = QLineEdit()
        txt_Password.setEchoMode(QLineEdit.Password)
        Login_Button = QPushButton("Login")
        Form_Layout = QFormLayout()
        Form_Layout.addRow(label_Username,txt_UserName)
        Form_Layout.addRow(label_Password,txt_Password)
        Form_Layout.addRow(Login_Button)
        self.setLayout(Form_Layout)


if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    myApp.exec_()