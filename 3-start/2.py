import sys
import time
from PySide2.QtWidgets import QApplication

from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QStatusBar
from PySide2.QtWidgets import QProgressBar
from PySide2.QtWidgets import QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("A Company Login Windows")
        self.setGeometry(300,250,400,300)
        
        #self.CreateStatusBar()
        self.CreateProgressBar()
        #self.showProgress()


    def CreateStatusBar(self):
        self.myStatusBar = QStatusBar()

        self.myStatusBar.showMessage('Ready',0)
        
        self.setStatusBar(self.myStatusBar)

    def CreateProgressBar(self):
        self.myStatusBar = QStatusBar()
        
        self.progressBar = QProgressBar()
        self.statusLabel = QLabel("Showing Progress")
        #self.finishLabel = QLabel("Finish Progress")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.myStatusBar.addWidget(self.statusLabel,1)
        self.myStatusBar.addWidget(self.progressBar,2)
        #self.myStatusBar.addWidget(self.finishLabel,3)

        self.setStatusBar(self.myStatusBar)

    def showProgress(self):
        while(self.progressBar.value() < self.progressBar.maximum()):
            self.progressBar.setValue(self.progressBar.value() + 10)
            time.sleep(1)
        self.statusLabel.setText('Ready') 




if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myMainWindow = MainWindow()
    myMainWindow.show()
    myApp.exec_()