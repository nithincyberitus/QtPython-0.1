import sys
from PySide2.QtWidgets import QApplication,QWidget,QListWidget,QStackedWidget,QHBoxLayout,QFormLayout
from PySide2.QtWidgets import QLineEdit,QRadioButton,QLabel,QCheckBox

class stackedExample(QWidget):
    def __init__(self):
        super(stackedExample,self).__init__()

        self.leftList = QListWidget()
        self.leftList.insertItem(0,'Contact')
        self.leftList.insertItem(1,'Personal')
        self.leftList.insertItem(2,'Educational')

        self.stack_1 = QWidget()
        self.stack_2 = QWidget()
        self.stack_3 = QWidget()

        self.stack_1_UI()
        self.stack_2_UI()
        self.stack_3_UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack_1)
        self.stack.addWidget(self.stack_2)
        self.stack.addWidget(self.stack_3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.leftList)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)
        self.leftList.currentRowChanged.connect(self.display)
        self.setGeometry(300,50,10,10)
        self.setWindowTitle("Stack Widget Demo")
        self.show()

    def stack_1_UI(self):
        layout = QFormLayout()
        layout.addRow("Name",QLineEdit())
        layout.addRow("Address",QLineEdit())
        #self.setTabText(0,"Contact Details")
        self.stack_1.setLayout(layout)
    
    def stack_2_UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"),sex)
        layout.addRow("Date of Birth",QLineEdit())
        self.stack_2.setLayout(layout)

    def stack_3_UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack_3.setLayout(layout)

    def display(self,i):
        self.stack.setCurrentIndex(i)

def main():
   app = QApplication(sys.argv)
   ex = stackedExample()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()