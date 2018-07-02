import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QTextEdit
#QWorkspcae Not Found




class MyMDIApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        workspace = QWorkspcae()
        workspace.setWindowTitle("Simple WorkSpace Example")
        for i in range(5):
            textEdit = QTextEdit()
            textEdit.setPlainText("Dummy Text " * 100)
            textEdit.setWindowTitle("Document %i" % i)
            workspace.addWindow(textEdit)
        workspace.tile()
        self.setCentralWidget(workspace)
        self.setGeometry(300, 300, 600, 350)
        self.show()

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = MyMDIApp()
    myWin.show()
    myApp.exec_()