import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QMessageBox

from Ui_showTime import Ui_Form_showTime
class MainWindow(QMainWindow,Ui_Form_showTime):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.Button_showTime.clicked.connect(self.show_time)

    def show_time(self):
        import time
        now = time.ctime()
        #self.label_showTime = QLabel(self)
        #self.label_showTime.setText("Hi")
        self.label_showTime.text(self,"Hi")
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()