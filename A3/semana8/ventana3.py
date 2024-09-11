import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventanamain.ui",self)
       
app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()