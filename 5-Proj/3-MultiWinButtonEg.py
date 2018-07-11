import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QHBoxLayout,QPushButton,QVBoxLayout,QDesktopWidget,QFrame,QGridLayout
from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QWindow
class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Multiple Window")
        #self.setGeometry(350,250,550,400)
        self.fg = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.fg.moveCenter(self.cp)
        self.move(self.fg.topLeft())
        self.setFixedSize(550,400)
        self.Set_CentralWidget()

    def Set_CentralWidget(self):
        self.layout = Main_Window_Layout()
        self.setCentralWidget(self.layout)

class Main_Window_Layout(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.Main_Layout = QHBoxLayout()
        self.Child_1 = Layout_Child_1()
        self.Child_2 = Layout_Child_2()
        self.Main_Layout.addWidget(self.Child_1)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Main_Layout.addWidget(self.line)
        self.Main_Layout.addWidget(self.Child_2)
        self.setLayout(self.Main_Layout)

class Layout_Child_1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.V_Layout_1 = QVBoxLayout()
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.V_Layout_1.addWidget(self.button_1)
        self.V_Layout_1.addWidget(self.button_2)
        self.setLayout(self.V_Layout_1)
        
        self.button_1.clicked.connect(self.show_window_1)
        self.button_2.clicked.connect(self.show_window_2)
        
        self.connect(self.button_1,SIGNAL('clicked()'),self.show_window_1)
        self.connect(self.button_2,SIGNAL('clicked()'),self.show_window_2)

    def show_window_1(self):
        print("Button 1 Pressed")
        new_Win_1 = Button_Window_1()
        new_Win_1.show()
        return

    def show_window_2(self):
        print("Button 2 Pressed")
        new_Win_2 = Button_Window_2()
        new_Win_2.show()
        return

class Layout_Child_2(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.V_Layout_2 = QVBoxLayout()
        self.button_3 = QPushButton("3")
        self.button_4 = QPushButton("4")        
        self.V_Layout_2.addWidget(self.button_3)
        self.V_Layout_2.addWidget(self.button_4)
        self.setLayout(self.V_Layout_2)

        self.button_3.clicked.connect(self.show_window_3)
        self.button_4.clicked.connect(self.show_window_4)
        
        self.connect(self.button_3,SIGNAL('clicked()'),self.show_window_3)
        self.connect(self.button_4,SIGNAL('clicked()'),self.show_window_4)

    def show_window_3(self):
        print("Button 3 Pressed")
        new_Button_3 = Button_Window_3()
        new_Button_3.show()
        return

    def show_window_4(self):
        print("Button 4 Pressed")
        new_Button_4 = Button_Window_4()
        new_Button_4.show()
        return

class Button_Window_1(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.show()
        

class Button_Window_2(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.show()

    def close(self):
        print("Waiting Over")
        return

class Button_Window_3(QWidget):
    def __init__(self):
        QWidget.__init__(self)

class Button_Window_4(QWidget):
    def __init__(self):
        QWidget.__init__(self)

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