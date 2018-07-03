import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QStatusBar,QWidget,QHBoxLayout,QFrame,QVBoxLayout,QFormLayout,QLabel,QLineEdit,QPushButton
from PySide2.QtCore import Qt,SIGNAL
from PySide2.QtGui import QPalette,QBrush,QPixmap

class Main_Window(QMainWindow):
    '''Our Main Class Window'''
    def __init__(self):
        '''Constructor Function'''
        QMainWindow.__init__(self)
        self.setWindowTitle("Login Window")
        #self.setWindowIcon(QIcon("company_logo.png"))
        self.setGeometry(350,250,550,400) #self.setGeometry(x,y,w,h)
        self.setUp_GUI()

    def setUp_GUI(self):
        '''Generate all UI Elements'''
        #Menubar
        self.Create_MenuBar()
        #Statusbar
        self.Create_StatusBar()
        #Toolbar
        #Dock Widget
        #Central Widget
        self.Create_CentralWidget()
        return

    def Create_MenuBar(self):
        #Menu Bar Item Creation
        '''Function to Create Actual Menu Bar'''
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def Create_StatusBar(self):
        '''Function to Create Status Bar'''
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage("Getting Ready",2000)
        self.setStatusBar(self.myStatusBar)
    
    def Create_ToolBar(self):
        return

    def Create_DockWidget(self):
        return

    def Create_CentralWidget(self):
        self.Main_Layout = Layout_Main_Window()
        self.setCentralWidget(self.Main_Layout)

class Layout_Main_Window(QWidget):
    '''Our Main Layout in Main Window'''
    def __init__(self,parent=None):
        '''Constructor Function'''
        QWidget.__init__(self,parent)
        self.Main_Layout = QHBoxLayout()
        self.Child_1 = Layout_Child_1()
        self.Child_2 = Layout_Child_2()
        self.Main_Layout.addWidget(self.Child_1)
        # Add a Saperator
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        self.Main_Layout.addWidget(line)
        self.Main_Layout.addWidget(self.Child_2)
        self.setLayout(self.Main_Layout)

class Layout_Child_1(QFrame):
    '''Our Image Display OR Text Display'''
    def __init__(self,parent=None):
        '''Constructor Function'''
        #QWidget.__init__(self,parent)
        QFrame.__init__(self)
        self.setUp_Login_UI()

    def setUp_Login_UI(self):
        self.palette = QPalette()
        self.pixmap = QPixmap("sec_shield.png")
        self.brush = QBrush()
        self.frame_layout = QVBoxLayout()
        self.setFixedSize(300,300)
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(4)
        self.setLayout(self.frame_layout)
        self.palette.setBrush(QPalette.Background,self.brush)
        self.setPalette(self.palette)
        
class Layout_Child_2(QWidget):
    '''Our Login Form Display'''
    def __init__(self,parent=None):
        '''Constructor Function'''
        QWidget.__init__(self,parent)
        self.setUp_Login_UI()

    def setUp_Login_UI(self):
        self.Login_Form = QFormLayout()
        self.setFixedSize(300,300)
        self.Label_User_Name = QLabel("User Name:")
        self.Label_User_Password = QLabel("Password")
        self.Txt_User_Name = QLineEdit()
        self.Txt_User_Password = QLineEdit()
        self.Txt_User_Password.setEchoMode(QLineEdit.Password)
        self.Button_Login = QPushButton("Login")
        self.Login_Form.addRow(self.Label_User_Name,self.Txt_User_Name)
        self.Login_Form.addRow(self.Label_User_Password,self.Txt_User_Password)
        self.Login_Form.addRow(self.Button_Login)
        self.Login_Form.setFormAlignment(Qt.AlignCenter)
        self.setLayout(self.Login_Form)

        self.connect(self.Button_Login,SIGNAL("clicked()"),self.Check_Login)

    def Check_Login(self):
        #user_name = self.Txt_User_Name()
        #user_password = self.Txt_User_Password()
        return

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWin = Main_Window()
        myWin.show()
        myApp.exec_()
    except NameError:
        print("Name Error:",sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])