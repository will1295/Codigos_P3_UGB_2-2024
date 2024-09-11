from PyQt5.QtWidgets import (QApplication,QWidget
                             ,QMainWindow,QPushButton,QLineEdit,
                             QVBoxLayout,QLabel)
import sys

class vprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana")
        self.setGeometry(350,100,500,500)
        boton = QPushButton("Haz click")
        self.texto = QLineEdit()
        self.label = QLabel("Este es un label")
        #self.textoedit = texto.text()
        layout = QVBoxLayout()
        central = QWidget(self)
        central.setLayout(layout)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_click)
        layout.addWidget(boton)
        layout.addWidget(self.texto)
        layout.addWidget(self.label)
        self.setCentralWidget(central)
       
    
    def boton_click(self):
        #print(self.texto.text())
        self.label.setText(self.texto.text())



app = QApplication(sys.argv)
ventana = vprincipal()
ventana.show()
app.exec()