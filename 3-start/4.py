import sys

from PySide2.QtWidgets import QApplication

from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QPushButton
class Vertical_Layout(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        

    def SetLayout(self):
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
    myLayout = Vertical_Layout()
    myLayout.SetLayout()
    myLayout.show()
    myApp.exec_()

    