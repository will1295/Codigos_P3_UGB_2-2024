from PIL import Image
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import io

def convertir(imagen):
    arreg = io.BytesIO()
    imagen.save(arreg,format="JPEG")
    imagenv = QPixmap()
    imagenv.loadFromData(arreg.getvalue())
    return imagenv

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Imagen en ventana")
#imagen = Image.open("imagenes/img.png")
imagen = Image.open("tigre.jpeg").resize((300,200))
mapapix = convertir(imagen)

label = QLabel()
label.setPixmap(mapapix)

layout = QVBoxLayout()
layout.addWidget(label)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec())