import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLayout
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,QPushButton
    ,QVBoxLayout,QWidget,QGridLayout,QFormLayout)

class main_ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,500,500)
        self.setWindowTitle("Mi primera ventana")
        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QGridLayout()
        boton = QPushButton("Boton1")
        boton2 = QPushButton("Boton2")
        boton3 = QPushButton("Boton3")
        layout.addWidget(boton,0,0)
        layout.addWidget(boton2,1,1)
        layout.addWidget(boton3,2,2)
        #self.setLayout(layout)
        central.setLayout(layout)

        
        
        #self.setCentralWidget(boton)

app = QApplication(sys.argv)
ventana = main_ventana()
ventana.show()
app.exec()