import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QGraphicsView,QGraphicsScene,QGraphicsEllipseItem,QTimeLine,QGraphicsItemAnimation,QGraphicsDropShadowEffect
from PySide2.QtCore import QPointF

class MyView(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        self.myScene = QGraphicsScene(self)
        self.myItem = QGraphicsEllipseItem(-20, -10, 50, 20)
        self.myScene.addItem(self.myItem)
        self.setScene(self.myScene)
        self.timeLine = QTimeLine(1000)
        self.timeLine.setFrameRange(0, 100)
        self.animate = QGraphicsItemAnimation()
        self.animate.setItem(self.myItem)
        self.animate.setTimeLine(self.timeLine)
        self.animate.setPosAt(0, QPointF(0, -10))
        self.animate.setRotationAt(1, 360)
        self.setWindowTitle("A Simple Animation")
        self.timeLine.start()
        self.effect = QGraphicsDropShadowEffect(self)
        self.effect.setBlurRadius(8)
        self.myItem.setGraphicsEffect(self.effect)
        self.myItem.setZValue(1)

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWin = MyView()
    MyView.show()
    myApp.exec_()