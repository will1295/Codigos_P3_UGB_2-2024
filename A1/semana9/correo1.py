import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

#Reemplaza con tus datos aqui
remit = os.getenv('CORREO')
serv = os.getenv('SERV')
puerto = os.getenv('PUERTO')
contra = os.getenv('CONTRA')

try:
    conex = smtplib.SMTP(serv,puerto)
    conex.starttls()
    conex.login(remit,contra)
    conex.sendmail(remit,remit,"Subject: Probando correo" 
                    "\n\n Este correo es automatico")
    print("El correo se ha mandado correctamente")
except smtplib.SMTPException as e:
    print(f"Error al mandar el mensaje: {e}")
finally:
    conex.quit()