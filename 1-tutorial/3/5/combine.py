import sys
import platform

import PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QTextEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QMessageBox

__version__ = '0.0.2'

from ui_combine import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.actionShow_GPL.triggered.connect(self.showGPL)
        
        self.action_About.triggered.connect(self.about)

        def showGPL(self):
            '''Read and Display GPL License'''
            self.textEdit.setText(open('COPYING.txt').read())

        def about(self):
            '''Popup a box with about message.'''
            QMessageBox.about(self, "About PyQt, Platform and the like",
                        """<b> About this program </b> v %s
                        <p>Copyright &copy; 2010 Joe Bloggs.
                        All rights reserved in accordance with
                        GPL v2 or later - NO WARRANTIES!
                        <p>This application can be used for
                        displaying OS and platform details.
                        <p>Python %s - PySide version %s - Qt version %s on s"""
                        (__version__, platform.python_version(),PySide2.__version__, PySide2.QtCore.__version__, platform.system()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()