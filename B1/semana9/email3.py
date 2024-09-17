import sys
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QVBoxLayout,QLabel,
                             QLineEdit,QTextEdit,QPushButton,QMessageBox)

class emailwind(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Envio de correos")
        self.setGeometry(100,100,400,300)
        layout = QVBoxLayout()
        self.lbldest = QLabel("Destinatario")
        self.lblasun = QLabel("Asunto")
        self.lblmens = QLabel("Mensaje")
        self.lindest = QLineEdit()
        self.linasun = QLineEdit()
        self.boxmens = QTextEdit()
        self.btnenv = QPushButton("Enviar",self)
        #layout.addWidget(self.lbldest)
        #layout.addWidget(self.lblasun)
        #layout.addWidget(self.lblmens)
        #layout.addWidget(self.lindest)
        #layout.addWidget(self.linasun)
        #layout.addWidget(self.boxmens)
        #layout.addWidget(self.btnenv)
        self.btnenv.clicked.connect(self.fcorreo)
        elemnts = [self.lbldest,self.lindest,self.lblasun,self.linasun,
                   self.lblmens,self.boxmens,self.btnenv]
        for el in elemnts:
            layout.addWidget(el)
        self.setLayout(layout)

    def fcorreo(self):
        servidor = os.getenv('SERVIDOR')
        puerto = os.getenv('PUERTO')
        correo = os.getenv('CORREO')
        contr = os.getenv('CONTRA')

        try:
            conec = smtplib.SMTP(servidor,puerto)
            conec.starttls()
            conec.login(correo,contr)
            dest = self.lindest.text()
            asun = self.linasun.text()
            mens = self.boxmens.toPlainText()
            conec.sendmail(correo,dest,f"Subject: {asun}"+
                            f"\n\n {mens}")
            print("Correo enviado exitosamente")
            QMessageBox.information(self,"Envio","Correo enviado exitosamente",)  
        except smtplib.SMTPException as e:
            print(f"Error al mandar el correo {e}")
            QMessageBox.critical(self,"Envio","Error al mandar el correo")  
 
        finally:
            conec.quit()

app = QApplication(sys.argv)
ventana = emailwind()
ventana.show()
app.exec()



        

