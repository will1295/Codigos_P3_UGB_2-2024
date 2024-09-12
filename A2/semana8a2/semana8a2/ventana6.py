from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QPushButton,QLabel,QLineEdit,QGridLayout,QWidget)
import sys

class vprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana de pyqt") 
        self.setGeometry(300,200,400,400)
        layout = QGridLayout()
        central = QWidget(self)
        texto = QLabel("Esto es un horizontal layout")
        entrada = QLineEdit()
        boton = QPushButton("Haz click acá")
        layout.addWidget(texto,0,0)
        layout.addWidget(entrada,1,1)
        layout.addWidget(boton,2,2)
        central.setLayout(layout)
        self.setCentralWidget(central)
  
        

app = QApplication(sys.argv)
ventana = vprincipal()
ventana.show()
app.exec()