import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QLineEdit,QGridLayout,QWidget)

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.setGeometry(500,200,400,400)
        central = QWidget()
        layout = QGridLayout()
        boton1 = QLineEdit()
        boton2 = QLineEdit()
        boton3 = QLineEdit("Boton 3",self)
        layout.addWidget(boton1,0,0)
        layout.addWidget(boton2,1,1)
        layout.addWidget(boton3,2,2)
        central.setLayout(layout)
        central.setGeometry(0,0,100,100)
        self.setCentralWidget(central)


app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()