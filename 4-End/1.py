import sys
import time
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QStatusBar, QProgressBar, QToolBar
from PySide2.QtWidgets import QLabel, QTextEdit
from PySide2.QtWidgets import QMenu, QAction, QMessageBox
from PySide2.QtGui import QIcon, QKeySequence


class Main_Window(QMainWindow):
    '''Our Main Window Class'''

    def __init__(self):
        '''Constructure Function'''
        QMainWindow.__init__(self)
        self.setWindowTitle("A Sample Text Editor")
        self.setWindowIcon(QIcon('doc_open.png'))
        self.setGeometry(350, 250, 550, 400)  # self.setGeometry(x,y,w,h)
        #self.setMinimumSize(250,250)# Size -> Width * Height
        #self.setMaximumSize(750,750)
        self.CreateStatusBar()
        #self.CreateProgressBar()
        #self.showProgress()
        self.setUpComponents()

    def setUpComponents(self):
        '''Setting Up Central Widget'''
        self.textEdit = QTextEdit("Enter your Text Here")
        self.setCentralWidget(self.textEdit)

        self.CreateActions()
        self.CreateMenus()
        self.CreateToolBar()

        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.pasteAction)
        self.fileMenu.addAction(self.aboutAction)

        self.mainToolbar.addAction(self.newAction)
        self.mainToolbar.addSeparator()
        self.mainToolbar.addAction(self.copyAction)
        self.mainToolbar.addAction(self.pasteAction)

    def CreateToolBar(self):
        '''Function to Create Toolbar'''
        self.mainToolbar = self.addToolBar('Main')

    #Slots Menu When Menu actions are Triggered
    def newFile(self):
        self.textEdit.setText('')

    def exitFile(self):
        self.close()

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This Example Demonstrate the Use of Menu Bar")

    def CreateActions(self):
        '''Functions to Create actions for Menus'''
        self.newAction = QAction(QIcon('doc_open.png'), '&New', self, shortcut=QKeySequence.New,
                                 statusTip='Create a New File', triggered=self.newFile)
        self.exitAction = QAction(QIcon('doc_open.png'), 'E&xit', self, shortcut="Ctrl+Q",
                                  statusTip="Exit the Application", triggered=self.exitFile)
        self.copyAction = QAction(QIcon("doc_open.png"), 'C&opy', self,
                                  shortcut="Ctrl+c", statusTip="Copy", triggered=self.textEdit.copy)
        self.pasteAction = QAction(QIcon('paste.png'), '&Paste', self,
                                   shortcut="Ctrl+V", statusTip="Paste", triggered=self.textEdit.paste)
        self.aboutAction = QAction(QIcon('about.png'), 'A&bout', self,
                                   statusTip="Displays info about text editor", triggered=self.aboutHelp)

    def CreateMenus(self):
        #Actual Menu Bar Item Creation
        '''Function to Create actual menu bar'''
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def showProgress(self):
        '''Function to Show Progress'''
        self.CreateProgressBar()
        while(self.progressbar.value() < self.progressbar.maximum()):
            self.progressbar.setValue(self.progressbar.value() + 10)
            time.sleep(0.5)
        self.myProgressMessage.setText("Ready")

    def CreateProgressBar(self):
        '''Function to Create Progrss Bar'''
        self.myProgressMessage = QLabel("In Progress")
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.myProgressStatusBar = QStatusBar()
        self.progressbar.setValue(0)
        self.myProgressStatusBar.addWidget(self.myProgressMessage, 1)
        self.myProgressStatusBar.addWidget(self.progressbar, 2)
        self.setStatusBar(self.myProgressStatusBar)

    def CreateStatusBar(self):
        '''Function to Create Status Bar'''
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage("Getting Ready", 2000)
        self.setStatusBar(self.myStatusBar)


if __name__ == '__main__':
    #Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWin = Main_Window()
        myWin.show()
        #myWin.showProgress()
        myApp.exec_()
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
