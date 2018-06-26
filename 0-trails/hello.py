import sys
from PySide2.QtWidgets import QApplication, QLabel

def intro_1():
    app = QApplication([])
    label = QLabel("Hello Qt for Python")
    label.show()
    app.exec_()
    #sys.exit(app.exec_())

def intro_2():
    app = QApplication([])
    label = QLabel()
    label.setText("Hello World")
    label.resize(800,600)
    label.show()
    app.exec_()

if __name__ == '__main__':
    #intro_1()
    intro_2()