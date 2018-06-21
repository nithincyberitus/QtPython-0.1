import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication,QWidget

class MyLogin(QWidget):
    def __init__(self):
        QWidget.__init__(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MyLogin()
    login.resize(800,600)
    login.show()
    sys.exit(app.exec_())