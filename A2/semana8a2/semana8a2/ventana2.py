from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys

class vprincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana de pyqt") 
        self.setGeometry(300,200,400,400)
        boton = QPushButton("Esto es un boton")
        self.setCentralWidget(boton)
        

app = QApplication(sys.argv)
ventana = vprincipal()
ventana.show()
app.exec()