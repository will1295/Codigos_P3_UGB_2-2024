import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton

class main_ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,300,300)
        self.setWindowTitle("Mi primera ventana")
        boton = QPushButton("Un boton")
        self.setCentralWidget(boton)

app = QApplication(sys.argv)
ventana = main_ventana()
ventana.show()
app.exec()