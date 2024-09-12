import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtWidgets,uic

class ventanap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eventos de PyQt5")
        self.setGeometry(300,400,300,300)
        uic.loadUi("interfazsuma.ui",self)
        self.boton = self.findChild(QtWidgets.QPushButton,"pushButton")
        self.num1 = self.findChild(QtWidgets.QLineEdit,"editnum1")
        self.num2 = self.findChild(QtWidgets.QLineEdit,"editnum2")
        self.boton.clicked.connect(self.sumar)

    def sumar(self):
        total = (int(self.num1.text()))+(int(self.num2.text()))
        print(total)
        

app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()