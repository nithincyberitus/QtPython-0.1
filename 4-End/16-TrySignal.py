import sys
from PySide2 import QtCore,QtGui
from PySide2.QtWidgets import QApplication,QPushButton

# Define a function that will be used as a slot
def sayHello():
    print("Hello World")

app = QApplication(sys.argv)
button = QPushButton("Say Hello")

#Connect the Clicked Signal to sayHello slot
button.clicked.connect(sayHello)
button.show()

sys.exit(app.exec_())