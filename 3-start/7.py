import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QProgressBar

from PySide2.QtWidgets import QFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        Main_Layout = Zero_Layout()
        self.setCentralWidget(Main_Layout)


class Zero_Layout(QWidget):
    def __init__(self):
        super(Zero_Layout,self).__init__()
        First = First_Layout()
        Second = Second_Layout()
        Third = Third_Layout()

        H_layout = QHBoxLayout()
        
        H_layout.addWidget(First)
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        H_layout.addWidget(line)
        #H_layout.addWidget(Second)
        H_layout.addWidget(Third)
        self.setLayout(H_layout)


class First_Layout(QWidget):
    def __init__(self):
        super(First_Layout,self).__init__()
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button1)
        V_Layout.addWidget(button2)
        self.setLayout(V_Layout)


class Second_Layout(QWidget):
    def __init__(self):
        super(Second_Layout,self).__init__()

class Third_Layout(QWidget):
    def __init__(self):
        super(Third_Layout,self).__init__()
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        V_Layout = QVBoxLayout()
        V_Layout.addWidget(button3)
        V_Layout.addWidget(button4)
        self.setLayout(V_Layout)

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    myApp.exec_()