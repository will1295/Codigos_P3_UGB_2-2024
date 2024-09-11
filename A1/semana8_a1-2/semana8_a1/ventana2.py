from PyQt5.QtWidgets import  QApplication,QWidget,QMainWindow,QPushButton
import sys
from PyQt5 import uic

#from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QGridLayout,QFormLayout

class ventana_main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("designs/ventanadesign.ui",self)
      

app = QApplication(sys.argv)
ventana = ventana_main()
ventana.show()
app.exec()