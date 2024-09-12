from PyQt5.QtWidgets import (QApplication
                             ,QMainWindow,QWidget,
                             QPushButton,QLineEdit,
                             QFormLayout,QLabel)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        boton = QPushButton("Haz click aqui")
        boton.clicked.connect(self.boton_click)
        self.edit = QLineEdit()
        self.label = QLabel()
        layout = QFormLayout()
        central = QWidget()
        layout.addRow(boton,self.edit)
        layout.addRow(self.label)
        central.setLayout(layout)
        self.setCentralWidget(central)
    
    def boton_click(self):
        #print("Haz hecho click")
        texto = self.edit.text()
        #print(texto)
        self.label.setText(texto)
   

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()