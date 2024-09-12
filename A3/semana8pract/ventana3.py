import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QWidget,QPushButton,QLineEdit,
                             QComboBox,QLabel)

from PyQt5 import uic

#Signals de pyqt5
# clicked, textChanged, toggled, valueChanged

class ventanam(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design1.ui",self)
        self.boton = self.findChild(QPushButton,"btnSuma")
        self.boton.clicked.connect(self.evento_click)
        self.num1 = self.findChild(QLineEdit,"num1")
        self.num2 = self.findChild(QLineEdit,"num2")
        self.lblr = self.findChild(QLabel,"label")
        self.combo = self.findChild(QComboBox,"comboBox")
        

    def evento_click(self):
       opcion = self.combo.currentText()
       n1 = int(self.num1.text())
       n2 = int(self.num2.text())
       if (opcion=="suma"):
        self.lblr.setText(str(n1+n2))
       elif(opcion=="resta"):
          self.lblr.setText(str(n1-n2))
          
       


app = QApplication(sys.argv)
ventana = ventanam()
ventana.show()
app.exec()