import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        component = C_Layout()
        self.setCentralWidget(component)

class C_Layout(QWidget):
    def __init__(self):
        super(C_Layout,self).__init__()
        layout = QVBoxLayout()
        A = A_Layout()
        B = B_Layout()
        layout.addWidget(A)
        layout.addWidget(B)
        self.setLayout(layout)


class B_Layout(QWidget):
    def __init__(self):
        super(B_Layout,self).__init__()
        button1 =  QPushButton("One")
        button2 =  QPushButton("Two")
        button3 =  QPushButton("Three")
        button4 =  QPushButton("Four")
        button5 =  QPushButton("Five")
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        self.setLayout(layout)

class A_Layout(QWidget):
    def __init__(self):
        super(A_Layout,self).__init__()
        button1 =  QPushButton("One")
        button2 =  QPushButton("Two")
        button3 =  QPushButton("Three")
        button4 =  QPushButton("Four")
        button5 =  QPushButton("Five")
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        self.setLayout(layout)


if __name__ == '__main__':
    myApp = QApplication(sys.argv)

    myWindow = MainWindow()
    myWindow.show()

    myApp.exec_()


