from PyQt5.QtWidgets import (QApplication,QWidget,
                             QLabel,QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PIL import Image
import sys
import io

def convertir(imagen):
    arreglo = io.BytesIO()
    imagen.save(arreglo,format="PNG")
    imagb = QPixmap()
    imagb.loadFromData(arreglo.getvalue())
    return imagb

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Ventana")
img = Image.open("img.png").resize((200,200))
label = QLabel()

imgv = convertir(img)
label.setPixmap(imgv)
layout = QVBoxLayout()
layout.addWidget(label)
ventana.setLayout(layout)
ventana.show()

sys.exit(app.exec())
