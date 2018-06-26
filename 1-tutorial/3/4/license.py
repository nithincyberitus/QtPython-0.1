import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QTextEdit
from PySide2.QtWidgets import QPushButton

from ui_license import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        '''Mandatory Initialisation of a Class.'''
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.showButton.clicked.connect(self.fileRead)

    def fileRead(self):
        '''Read and Display License'''

        self.textEdit.setText(open('COPYING.txt').read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()