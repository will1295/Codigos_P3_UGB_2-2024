import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QPushButton,QLabel,QGridLayout,QWidget,QLineEdit)

class ventanap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eventos de PyQt5")
        self.setGeometry(300,400,300,300)
        layout = QGridLayout()
        central = QWidget()
        label = QLabel("Evento de click",self)
        boton = QPushButton("Haz click",self)
        txtedit = QLineEdit()
        txtedit.textChanged.connect(self.eventotxtchang)
        #Signal del evento click
        boton.clicked.connect(self.eventoclick)
        layout.addWidget(label,0,0)
        layout.addWidget(boton,0,1)
        layout.addWidget(txtedit,1,0)
        central.setLayout(layout)
        self.setCentralWidget(central)

    #Slot del evento click
    def eventoclick(self):
        print("Haz hecho click al boton")

    def eventotxtchang(self):
        print("Se ha escrito algo en el edit")

app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()