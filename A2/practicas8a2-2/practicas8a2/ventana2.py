import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtWidgets,uic

class ventanap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eventos de PyQt5")
        self.setGeometry(300,400,300,300)
        uic.loadUi("interfaz.ui",self)
        self.boton = self.findChild(QtWidgets.QPushButton,"pushButton")
        self.txt = self.findChild(QtWidgets.QLineEdit,"lineEdit")
        self.etiqueta = self.findChild(QtWidgets.QLabel,"label_2")
        self.boton.clicked.connect(self.cambiartxt)

    def cambiartxt(self):
        #print("Hola!")
        self.etiqueta.setText(self.txt.text())
        

    #Slot del evento click
    def eventoclick(self):
        print("Haz hecho click al boton")

    def eventotxtchang(self):
        print("Se ha escrito algo en el edit")

app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()