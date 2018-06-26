import sys

from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QApplication

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QMessageBox

from Ui_showDateTime import Ui_ShowDateTime

class MainWindow(QMainWindow,Ui_ShowDateTime):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        
        self.ShowDate.clicked.connect(self.showdate)
        self.showTime.clicked.connect(self.showtime)
        self.show_Date_Time.clicked.connect(self.showdatetime)

    def showdate(self):
        QMessageBox.ShowDate(self,"Let's Show Date")
    
    def showtime(self):
        QMessageBox.showTime(self,"Let's Show Time")
    def showdatetime(self):
        QMessageBox.show_Date_Time(self,"Let's show Date and Time")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()