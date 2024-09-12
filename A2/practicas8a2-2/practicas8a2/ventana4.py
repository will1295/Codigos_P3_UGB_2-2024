import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtWidgets,uic

class ventanap(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.resize(100, 100)
        self.setWindowTitle('Alejandro')
        self.setStyleSheet('background-color: green;')

app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()