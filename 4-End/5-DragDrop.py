import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget,QListWidget,QHBoxLayout,QListWidgetItem
from PySide2.QtGui import QIcon

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()
        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)
        self.setGeometry(300, 350, 500, 150)
        self.myLayout = QHBoxLayout()
        self.myLayout.addWidget(self.myListWidget1)
        self.myLayout.addWidget(self.myListWidget2)
        self.l1 = QListWidgetItem(QIcon('doc_saved.png'),"Angry Bird Blue")
        self.l2 = QListWidgetItem(QIcon('doc_saved.png'),"Angry Bird Red")
        self.l3 = QListWidgetItem(QIcon('doc_saved.png'),"Angry Bird Green")
        self.l4 = QListWidgetItem(QIcon('doc_saved.png'),"Angry Bird Black")
        self.l5 = QListWidgetItem(QIcon('doc_saved.png'),"Angry Bird White")
        self.myListWidget1.insertItem(1,self.l1)
        self.myListWidget1.insertItem(2,self.l2)
        self.myListWidget1.insertItem(3,self.l3)
        self.myListWidget1.insertItem(4,self.l4)
        self.myListWidget1.insertItem(5,self.l5)
        QListWidgetItem(QIcon('doc_write.png'), "Grey Pig", self.myListWidget2)
        QListWidgetItem(QIcon('doc_write.png'), "Brown Pig", self.myListWidget2)
        QListWidgetItem(QIcon('doc_write.png'), "Green Pig", self.myListWidget2)
        self.setWindowTitle('Drag and Drop Example')
        self.setLayout(self.myLayout)


if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = MyWidget()
    myWin.show()
    myApp.exec_()