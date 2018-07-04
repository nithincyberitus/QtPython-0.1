import sys
from PySide2.QtWidgets import QApplication,QPushButton
from PySide2.QtCore import Signal,Slot,QObject
'''
#Add some overloads.
#A small modification of the previous example, now with overloaded decorators.

#Defines a slot that recieves a C 'int' or 'str'
#and has 'saySomething' as its name
@Slot(int)
@Slot(str)
def saySomething(stuff):
    print(stuff)

class Communicate(QObject):
    #Create new signals on the fly: One will handle
    # int type, the other will handle string type
    speak_number = Signal(int)
    speak_word = Signal(str)

someone = Communicate()
#Connect signal to slot properly
someone.speak_number.connect(saySomething)
someone.speak_word.connect(saySomething)
#Emit each 'speak' signal
someone.speak_word.emit("Hello Everyone")
someone.speak_number.emit(95)
'''


#An example with slot overloads and more complicated signal connections and emissions:
app = QApplication(sys.argv)
# define a new slot that receives a C 'int' or a 'str'
# and has 'saySomething' as its name
@Slot(int)
@Slot(str)
def say_something(stuff):
    print(stuff)
class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = Signal((int,), (str,))
someone = Communicate()
# connect signal and slot. As 'int' is the default
# we have to specify the str when connecting the
# second signal
someone.speak.connect(say_something)
someone.speak[str].connect(say_something)
# emit 'speak' signal with different arguments.
# we have to specify the str as int is the default
someone.speak.emit(10)
someone.speak[str].emit("Hello everybody!")