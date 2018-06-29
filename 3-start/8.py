import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGridLayout

from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        Main = Main_Widget()
        self.setCentralWidget(Main)

class Main_Widget(QWidget):
    def __init__(self):
        super(Main_Widget,self).__init__()
        First = First_Widget()
        Second = Second_Widget()
        Third = Third_Widget()
        Fourth = Four_Widget()

        H_Layout = QHBoxLayout()
        H_Layout.addWidget(First)
        H_Layout.addWidget(Second)
        H_Layout.addWidget(Third)
        H_Layout.addWidget(Fourth)
        self.setLayout(H_Layout)
        
class First_Widget(QWidget):
    def __init__(self):
        super(First_Widget,self).__init__()
        button1 = QPushButton("One")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button1,0,0)
        self.setLayout(V_Layout)

class Second_Widget(QWidget):
    def __init__(self):
        super(Second_Widget,self).__init__()
        button2 = QPushButton("Two")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button2,0,0)
        self.setLayout(V_Layout)

class Third_Widget(QWidget):
    def __init__(self):
        super(Third_Widget,self).__init__()
        button3 = QPushButton("Three")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button3,0,0)
        self.setLayout(V_Layout)

class Four_Widget(QWidget):
    def __init__(self):
        super(Four_Widget,self).__init__()
        button4 = QPushButton("Four")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button4,0,0)
        self.setLayout(V_Layout)

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = QMainWindow()
    myWin.show()
    myApp.exec_()