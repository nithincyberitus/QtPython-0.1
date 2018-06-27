import sys
from PySide2.QtWidgets import QApplication
#from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Simple Login Windows")
        self.setGeometry(300,250,400,300)
        

    def SetLayout(self):
        formLayout = QFormLayout()
        labelUsername = QLabel("Username")
        txtUsername = QLineEdit()
        labelPassword = QLabel("Password")
        txtPassword = QLineEdit()
        txtPassword.setEchoMode(QLineEdit.Password)
        loginButton = QPushButton("&Login",self)
        formLayout.addRow(labelUsername,txtUsername)
        formLayout.addRow(labelPassword,txtPassword)
        formLayout.addRow(loginButton)
        self.setLayout(formLayout)



if __name__ == '__main__':

    myApp = QApplication(sys.argv)
    loginWin = LoginWindow()

    loginWin.SetLayout()
    
    loginWin.show()
    myApp.exec_()
    sys.exit(0)