import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QDesktopWidget
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QFrame
from PySide2.QtWidgets import QLabel, QLineEdit, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QImage, QPixmap


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.main_widget = Main_Widget(self)
        self.setCentralWidget(self.main_widget)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Welcome")
        self.fg = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.fg.moveCenter(self.cp)
        self.move(self.fg.topLeft())
        self.setFixedSize(550, 400)


class Main_Widget(QWidget):
    def __init__(self, parent=None):
        super(Main_Widget, self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        layout = QHBoxLayout()
        self.stack = QStackedWidget(parent=self)
        self.welcome = Welcome_Widget(parent=self)
        self.welcome.login.Button_Login.clicked.connect(
            self.check_user_details)
        self.user = User_Widget(parent=None)
        self.user.Button_Quit.clicked.connect(self.user_quit)
        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.user)
        layout.addWidget(self.stack)

    def check_user_details(self):
        self.stack.setCurrentWidget(self.user)

    def user_quit(self):
        self.stack.setCurrentWidget(self.welcome)


class Welcome_Widget(QWidget):
    def __init__(self, parent=None):
        super(Welcome_Widget, self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.layout = QHBoxLayout()

        self.image = Image_Widget(self)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.login = Login_Widget(self)

        self.layout.addWidget(self.image)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.login)

        self.setLayout(self.layout)


class Image_Widget(QWidget):
    def __init__(self, parent=None):
        super(Image_Widget, self).__init__(parent)
        self.label = QLabel()
        self.image = QImage('sec_shield.png')
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class Login_Widget(QWidget):
    def __init__(self, parent=None):
        super(Login_Widget, self).__init__(parent)

        self.Login_Form = QFormLayout()
        self.setFixedSize(250, 250)
        self.Label_User_Name = QLabel("User Name:")
        self.Label_User_Password = QLabel("Password:")
        self.Txt_User_Name = QLineEdit()
        self.Txt_User_Password = QLineEdit()
        self.Txt_User_Password.setEchoMode(QLineEdit.Password)
        self.Button_Login = QPushButton("Login")
        self.Login_Form.addRow(self.Label_User_Name, self.Txt_User_Name)
        self.Login_Form.addRow(self.Label_User_Password,
                               self.Txt_User_Password)
        self.Login_Form.addRow(self.Button_Login)
        self.Login_Form.setFormAlignment(Qt.AlignCenter)
        self.setLayout(self.Login_Form)


class User_Widget(QWidget):
    def __init__(self, parent):
        super(User_Widget, self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.Button_Quit = QPushButton('Quit', parent=self)


if __name__ == '__main__':
        try:
            myApp = QApplication(sys.argv)
            myWin = Main_Window()
            myWin.show()
            myApp.exec_()
        except NameError:
            print("Name Error: ", sys.exc_info()[1])
        except SystemExit:
            print("System Exit: ", sys.exc_info()[1])
        except Exception:
            print(sys.exc_info()[1])
