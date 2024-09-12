from PyQt5.QtWidgets import (QApplication
                             ,QMainWindow,QWidget,QLineEdit,
                             QPushButton,QLabel)
import sys
from PyQt5 import uic

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui",self)
        self.num1 = self.findChild(QLineEdit,"num1")
        self.num2 = self.findChild(QLineEdit,"num2")
        self.boton = self.findChild(QPushButton,"pushButton")
        self.label = self.findChild(QLabel,"lblresult")
        self.boton.clicked.connect(self.boton_click)
       
    
    def boton_click(self):
        num1 = int(self.num1.text())
        num2 = int(self.num2.text())
        self.label.setText(str(num1+num2))
   

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()