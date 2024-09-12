import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QWidget,QPushButton,QLineEdit,
                             QHBoxLayout)

#Signals de pyqt5
# clicked, textChanged, toggled, valueChanged

class ventanam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica Semana 8")
        boton = QPushButton("Haz click aqui")
        boton.clicked.connect(self.evento_click)
        inputxt = QLineEdit()
        inputxt.textChanged.connect(self.evento_txt)
        central = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(boton)
        layout.addWidget(inputxt)
        central.setLayout(layout)
        self.setCentralWidget(central)
        #self.setCentralWidget(boton)
    
    def evento_click(self):
        print("Haz hecho click!")

    def evento_txt(self):
         print("El texto ha cambiado!")

app = QApplication(sys.argv)
ventana = ventanam()
ventana.show()
app.exec()