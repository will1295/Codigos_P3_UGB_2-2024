import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    mensaje = MIMEMultipart()
    mensaje["Subject"] = "Asunto de mime mail"
    mensaje["From"] = remit
    mensaje["To"] = remit
    html = """
    <html>
        <body>
            <h1 style="color:blue">Este es un titulo</h1>
            <p>Esto es un parrafo</p>
        </body>
    </html>
    """
    menshtml = MIMEText(html,'html')
    mensaje.attach(menshtml)
    conex.sendmail(remit,remit,mensaje.as_string())
    print("El correo se ha mandado correctamente")
except smtplib.SMTPException as e:
    print(f"Error al mandar el mensaje: {e}")
finally:
    conex.quit()