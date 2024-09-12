from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
#from PyQt5 import uic
from PyQt5 import uic

class vprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uiventana.ui",self)
        

app = QApplication(sys.argv)
ventana = vprincipal()
ventana.show()
app.exec()