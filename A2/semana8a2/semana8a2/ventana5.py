from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QPushButton,QLabel,QLineEdit,QHBoxLayout,QWidget)
import sys

class vprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana de pyqt") 
        self.setGeometry(300,200,400,400)
        layout = QHBoxLayout()
        central = QWidget(self)
        texto = QLabel("Esto es un horizontal layout")
        entrada = QLineEdit()
        boton = QPushButton("Haz click acá")
        layout.addWidget(texto)
        layout.addWidget(entrada)
        layout.addWidget(boton)
        central.setLayout(layout)
        self.setCentralWidget(central)
  
        

app = QApplication(sys.argv)
ventana = vprincipal()
ventana.show()
app.exec()