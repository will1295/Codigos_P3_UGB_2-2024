from PyQt5.QtWidgets import  (QApplication,QWidget,QMainWindow,
                              QPushButton,QLabel,QGridLayout,QLineEdit)
import sys

class ventana_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana con pyqt5")
        self.setGeometry(100,200,300,300)
        central = QWidget()
        boton = QPushButton("Haz click aqui")
        texto = QLabel("Esto es un label")
        entrada = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(boton,0,0)
        layout.addWidget(texto,1,1)
        layout.addWidget(entrada,2,2)
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = ventana_main()
ventana.show()
app.exec()