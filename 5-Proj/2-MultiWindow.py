import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QStackedWidget,QPushButton,QHBoxLayout
from PySide2.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)

        self.initUI()

    def initUI(self):
        self.resize(300, 500)
        self.statusBar()
        self.statusBar().showMessage('Elo Elo')
        self.setWindowTitle('StartApp Welcome')

    # Instead of overriding this method you should look into using QActions instead.
    """ Esc zamyka program (keyPressEvent) """
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        else:
            # Don't forget to call the super class method otherwise any key
            # other than the escape key won't do anything.
            super(MainWindow, self).keyPressEvent(e)


# This class is where we handle switching between QStackedWidget pages
class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.stack = QStackedWidget(parent=self)

        self.search = SearchWidget(parent=self)
        self.search.searchButton.clicked.connect(self.goSearch)
        self.back = BackWidget(parent=self)
        self.back.backButton.clicked.connect(self.goBack)

        self.stack.addWidget(self.search)
        self.stack.addWidget(self.back)

        layout.addWidget(self.stack)

    def goSearch(self):
        self.stack.setCurrentWidget(self.back)

    def goBack(self):
        self.stack.setCurrentWidget(self.search)


class SearchWidget(QWidget):
    def __init__(self, parent=None):
        super(SearchWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.searchButton = QPushButton('searchButton', parent=self)
        optionButton = QPushButton('optionButton', parent=self)
        quitButton = QPushButton('quitButton', parent=self)
        listButton = QPushButton('listButton', parent=self)

        vbox = QVBoxLayout(self)
        vbox.addStretch(1)
        vbox.addWidget(self.searchButton)
        vbox.addWidget(optionButton)

        hbox = QHBoxLayout()
        hbox.addWidget(listButton)
        hbox.addWidget(quitButton)

        vbox.addLayout(hbox)


class BackWidget(QWidget):
    def __init__(self, parent=None):
        super(BackWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.backButton = QPushButton('GoBack', parent=self)


def main():
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()

if __name__ == '__main__':
    main()