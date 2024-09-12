import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QWidget,QPushButton,QLineEdit,
                             QHBoxLayout,QLabel)

#Signals de pyqt5
# clicked, textChanged, toggled, valueChanged

class ventanam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica Semana 8")
        boton = QPushButton("Haz click aqui")
        boton.clicked.connect(self.evento_click)
        self.inputxt = QLineEdit()
        self.texto = QLabel()
        central = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(boton)
        layout.addWidget(self.inputxt)
        layout.addWidget(self.texto)
        central.setLayout(layout)
        self.setCentralWidget(central)
        #self.setCentralWidget(boton)
    
    def evento_click(self):
       txtinp = self.inputxt.text()
       self.texto.setText(txtinp)


app = QApplication(sys.argv)
ventana = ventanam()
ventana.show()
app.exec()