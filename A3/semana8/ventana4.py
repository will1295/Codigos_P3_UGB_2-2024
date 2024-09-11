import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QPushButton,QVBoxLayout,QWidget)

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.setGeometry(500,200,400,400)
        central = QWidget()
        layout = QVBoxLayout()
        boton1 = QPushButton("Boton 1",self)
        boton2 = QPushButton("Boton 2",self)
        boton3 = QPushButton("Boton 3",self)
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        central.setLayout(layout)
        central.setGeometry(0,0,100,100)
        self.setCentralWidget(central)


app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()