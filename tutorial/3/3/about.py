import sys
import platform

import PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QTextEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QMessageBox

from ui_about import Ui_MainWindow

__version__ = '0.0.1'

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.aboutButton.clicked.connect(self.about)

    def about(self):
        '''Popup a box with about message'''
        QMessageBox.about(self,"About PySide, Platform and the like",
                            """<b>Platform Details</b> v {}
                            <p>Copyright &copy; 2018 Cyber-itus.
                            All rights reserved in accordance with Company.
                            This application is used for displaying personal details.
                            <p>Python {} - PySide2 version {} - Qt Version {} on {}
                            """.format(__version__,platform.python_version(),PySide2.__version__,PySide2.QtCore.__version__,platform.system()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()