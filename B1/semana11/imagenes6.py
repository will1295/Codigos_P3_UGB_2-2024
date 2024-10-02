from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel
import sys
import io

def imagenv(img):
    imgbyts = io.BytesIO()
    img.save(imgbyts,format="png")
    imgv = QPixmap()
    imgv.loadFromData(imgbyts.getvalue())
    return imgv

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Prueba")
imagen = Image.open("logo.png")
imgven = imagenv(imagen)
label = QLabel()
label.setPixmap(imgven)

layout = QVBoxLayout()
layout.addWidget(label)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec())