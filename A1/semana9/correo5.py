from PyQt5.QtWidgets import (QApplication,QMainWindow
                             ,QWidget,QLabel,
                             QLineEdit,QPushButton,
                             QMessageBox,QFormLayout,
                             QTextEdit)
import smtplib
import sys

class mainv(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Envio de correo")
        self.setGeometry(100,100,300,200)
        layout = QFormLayout()
        self.lbldest = QLabel("Destinatario")
        self.lblasunt = QLabel("Asunto")
        self.lblmensj = QLabel("Mensaje")
        self.editdest = QLineEdit()
        self.editdest.setPlaceholderText("Correo destino")
        self.editasun = QLineEdit()
        self.editmensj = QTextEdit()
        self.btnenv = QPushButton("Enviar mensaje")
        layout.addRow(self.lbldest,self.editdest)
        layout.addRow(self.lblasunt,self.editasun)
        layout.addRow(self.lblmensj,self.editmensj)
        layout.addRow(self.btnenv)
        self.setLayout(layout)
        self.btnenv.clicked.connect(self.enviar)

    def enviar(self):
        server = "smtp.gmail.com"
        puerto = 587
        correo = "monteswillian12@gmail.com"
        contra = "hnit bwkd efuw jqmz"
        try:
            conex = smtplib.SMTP(server,puerto)
            #print(conex.ehlo())
            conex.starttls()
            conex.login(correo,contra)
            conex.sendmail(correo,self.editdest.text(),f"Subject: {self.editasun.text()}"+
                        f"\n\n {self.editmensj.toPlainText()}")
            QMessageBox.information(self,"Envio","Enviado correctamente")
            
        except:
            QMessageBox.critical(self,"Envio","Error al enviar")
        finally:
            conex.quit()
    


app = QApplication(sys.argv)
ventana = mainv()
ventana.show()
app.exec()