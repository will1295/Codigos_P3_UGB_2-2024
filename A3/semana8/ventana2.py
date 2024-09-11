import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.setGeometry(500,200,400,400)
        boton = QPushButton("Push Button")
        self.setCentralWidget(boton)

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()