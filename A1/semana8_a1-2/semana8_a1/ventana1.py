from PyQt5.QtWidgets import  QApplication,QWidget,QMainWindow,QPushButton
import sys

class ventana_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana con pyqt5")
        self.setGeometry(100,200,300,300)
        boton = QPushButton("Haz click aqui")
        self.setCentralWidget(boton)

app = QApplication(sys.argv)
ventana = ventana_main()
ventana.show()
app.exec()