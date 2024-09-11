import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class miventana(QMainWindow):
    def __init__(self):
        super().__init__()
        #Linea para agregar archivos de interfaz
        uic.loadUi('ventana.ui',self)
        self.boton = self.findChild(QtWidgets.QPushButton,"botonClick")
        self.boton.clicked.connect(self.click_boton)
    
    def click_boton(self):
        print("Hola Mundo")

app = QApplication(sys.argv)
ventana = miventana()
ventana.show()
app.exec()