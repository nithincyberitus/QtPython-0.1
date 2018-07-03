import sys
from PySide2.QtWidgets import QApplication,QFrame,QVBoxLayout,QPushButton
from PySide2.QtGui import QPalette,QPixmap,QBrush
class MyMainWindow(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        palette = QPalette()
        pixmap = QPixmap("sec_shield.png")
        brush = QBrush(pixmap)
        frame_layout = QVBoxLayout()

        self.setFixedSize(300, 300)
        self.setFrameStyle(QFrame.Box)
        self.setWindowTitle("QFrame Set Background Image Example")

        #set QFrame Border Width 4 pixels
        self.setLineWidth(4)
        self.setLayout(frame_layout)

        btn1 = QPushButton(self)
        btn1.setText("Button 1")
        frame_layout.addWidget(btn1)
        palette.setBrush(QPalette.Background, brush)
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()