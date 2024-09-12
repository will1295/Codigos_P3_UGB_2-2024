from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QPushButton,QLabel,QLineEdit,QFormLayout,QWidget)
import sys

class vprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana de pyqt") 
        self.setGeometry(300,200,400,400)
        layout = QFormLayout()
        central = QWidget(self)
        texto = QLabel("Esto es un horizontal layout")
        entrada = QLineEdit()
        texto2 = QLabel("Esto es un form layout")
        entrada2 = QLineEdit()
        boton = QPushButton("Haz click acá")
        layout.addRow(texto,entrada)
        layout.addRow(texto2,entrada2)
        layout.addRow(boton)

        central.setLayout(layout)
        self.setCentralWidget(central)
  
        

app = QApplication(sys.argv)
ventana = vprincipal()
ventana.show()
app.exec()