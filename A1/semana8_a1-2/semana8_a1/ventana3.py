from PyQt5.QtWidgets import  (QApplication,QWidget,QMainWindow,
                              QPushButton,QLabel,QVBoxLayout,QLineEdit)
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
        layout = QVBoxLayout()
        layout.addWidget(boton)
        layout.addWidget(texto)
        layout.addWidget(entrada)
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = ventana_main()
ventana.show()
app.exec()