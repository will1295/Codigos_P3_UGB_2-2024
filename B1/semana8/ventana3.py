import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QMainWindow

class miventana(QMainWindow):
    def __init__(self):
        super().__init__()
        #Linea para agregar archivos de interfaz
        uic.loadUi('ventana.ui',self)

app = QApplication(sys.argv)
ventana = miventana()
ventana.show()
app.exec()