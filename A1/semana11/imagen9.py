from PIL import Image
from PyQt5.QtWidgets import (QApplication
                             ,QLabel,QWidget,QVBoxLayout)
from PyQt5.QtGui import QPixmap
import sys
import io

def convertir(imagen):
    arreglo = io.BytesIO()
    imagen.save(arreglo,format="png")
    imagenv = QPixmap()
    imagenv.loadFromData(arreglo.getvalue())
    return imagenv

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Imagen en ventana de pyqt5")
img = Image.open("tigre.png").resize((200,100))
mapa=convertir(img)
label = QLabel()
label.setPixmap(mapa)
layout = QVBoxLayout()
layout.addWidget(label)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec())
