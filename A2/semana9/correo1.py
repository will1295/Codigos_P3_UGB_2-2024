import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

correo = os.getenv("CORREO")
contra = os.getenv("CONTRA")
servi = os.getenv("SERVIDOR")
puerto = os.getenv("PUERTO")

try:
    conex = smtplib.SMTP(servi,puerto)
    conex.starttls()
    conex.login(correo,contra)
    conex.sendmail(correo,correo,"Subject:Probando smptplib\n\n"+
                "Estoy mandando este correo automaticamente por Python")
    conex.quit()
    print("El correo se ha enviado correctamente")
except smtplib.SMTPResponseException as e:
    print(f"Se ha encontrado un error: {e}")
