#import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
import sys

app = QApplication(sys.argv)
#ventana = QWidget()
#ventana.show()
boton = QPushButton("Haz click")
boton.show()
app.exec()