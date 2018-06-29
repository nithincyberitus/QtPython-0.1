import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget

from PySide2.QtWidgets import QLayout
from PySide2.QtWidgets import QBoxLayout
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QFormLayout

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        Layout_Main = Main_Layout()
        
        self.setCentralWidget(Layout_Main)

class Main_Layout(QWidget):
    def __init__(self):
        super(Main_Layout,self).__init__()
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")
        button6 = QPushButton("Six")

        
        #Element_Layout = QGridLayout()
        #Element_Layout.addWidget(button1,0,0)
        #Element_Layout.addWidget(button2,1,0)
        #First_Layout = Child_First_Layout()
        #Second_Layout = Child_Second_Layout()
        #Element_Layout.addLayout(First_Layout,0,0)
        #Element_Layout.addLayout(Second_Layout,1,0)

        Element_Layout = QHBoxLayout()
        Zero_Layout = Child_Zero_Layout()
        First_Layout = Child_First_Layout()
        Second_Layout = Child_Second_Layout()
        Fourth_Layout = Child_Form_Layout()

        Element_Layout.addWidget(Zero_Layout)
        Element_Layout.addWidget(First_Layout)
        Element_Layout.addWidget(Second_Layout)

        Element_Layout.addWidget(Fourth_Layout)

        self.setLayout(Element_Layout)

class Child_Zero_Layout(QWidget):
    def __init__(self):
        super(Child_Zero_Layout,self).__init__()
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        Z_Layout = QVBoxLayout()
        Z_Layout.addWidget(button1)
        Z_Layout.addWidget(button2)

        self.setLayout(Z_Layout)

class Child_First_Layout(QWidget):
    def __init__(self):
        super(Child_First_Layout,self).__init__()
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        H_Layout = QHBoxLayout()
        H_Layout.addWidget(button3)
        H_Layout.addWidget(button4)
        
        self.setLayout(H_Layout)

class Child_Second_Layout(QWidget):
    def __init__(self):
        super(Child_Second_Layout,self).__init__()
        button5 = QPushButton("Five")
        button6 = QPushButton("Six")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button5)
        V_Layout.addWidget(button6)
        
        self.setLayout(V_Layout)

class Child_Form_Layout(QWidget):
    def __init__(self):
        super(Child_Form_Layout,self).__init__()
        labelUserName = QLabel("User Name")
        txtUserName = QLineEdit()
        labelPassword = QLabel("Password")
        txtPassword = QLineEdit()
        txtPassword.setEchoMode(QLineEdit.Password)
        buttonLogin = QPushButton("Login")
        Form_Layout = QFormLayout()
        Form_Layout.addRow(labelUserName,txtUserName)
        Form_Layout.addRow(labelPassword,txtPassword)
        Form_Layout.addRow(buttonLogin)
        self.setLayout(Form_Layout)




if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    myApp.exec_()