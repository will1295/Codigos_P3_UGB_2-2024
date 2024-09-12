from PyQt5.QtWidgets import (QApplication
                             ,QMainWindow,QWidget,
                             QPushButton,QLineEdit)
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Haz click aqui")
        boton.clicked.connect(self.boton_click)
        edit = QLineEdit()
        edit.textChanged.connect(self.texto_cambiado)
        self.setCentralWidget(edit)
    
    def boton_click(self):
        print("Haz hecho click")

    def texto_cambiado(self):
        print("Haz escrito algo")    

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()