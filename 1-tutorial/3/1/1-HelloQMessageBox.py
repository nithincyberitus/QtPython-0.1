#!/usr/bin/python

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMessageBox

# Create the application object
app = QApplication(sys.argv)

#Create a simple dailog box
msg_box = QMessageBox()
msg_box.setText("Hello World!")
msg_box.show()

sys.exit(msg_box.exec_())