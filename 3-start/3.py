import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton

from PySide2.QtWidgets import QVBoxLayout

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("A Simple Login Window Client")
        self.setGeometry(100,100,800,600)




if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myMainWindow = MainWindow()
    myMainWindow.centralWidget()
    myMainWindow.show()
    myApp.exec_()