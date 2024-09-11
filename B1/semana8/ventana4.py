import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLayout
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,QPushButton
    ,QLayout,QVBoxLayout,QWidget,QHBoxLayout)
#QVBoxLayout es para layout verticales
#QHBoxLayout es para layout horizontales
class main_ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,300,300)
        self.setWindowTitle("Mi primera ventana")
        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        #layout = QGridLayout()
        boton = QPushButton("Boton1")
        boton2 = QPushButton("Boton2")
        boton3 = QPushButton("Boton3")
        layout.addWidget(boton)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        #self.setLayout(layout)
        central.setLayout(layout)

        
        
        #self.setCentralWidget(boton)

app = QApplication(sys.argv)
ventana = main_ventana()
ventana.show()
app.exec()