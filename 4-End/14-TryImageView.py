import sys
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView

class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.image = QPixmap("sec_shield.png")
        self.item = QGraphicsPixmapItem(self.image)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.show()

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = Main_Window()
    myWin.show()
    myApp.exec_()