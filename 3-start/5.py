import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import  QPushButton

class Horizontal_Layout(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def SetLayout(self):
        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
        button3 = QPushButton("button3")
        button4 = QPushButton("button4")
        button5 = QPushButton("button5")

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        self.setLayout(layout)

if __name__ == '__main__':

    myApp = QApplication(sys.argv)
    myLayout = Horizontal_Layout()
    myLayout.SetLayout()
    myLayout.show()
    myApp.exec_()