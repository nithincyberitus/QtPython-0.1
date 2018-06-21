import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("<font color=Blue size=200>Hello World!</font>")
label.show()
app.exec_()