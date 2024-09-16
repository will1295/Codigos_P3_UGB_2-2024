import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Reemplazar variables de entorno con tus valores
servidor = os.getenv('SERVIDOR')
puerto = os.getenv('PUERTO')
correo = os.getenv('CORREO')
contr = os.getenv('CONTRA')

try:
    conec = smtplib.SMTP(servidor,puerto)
    conec.starttls()
    conec.login(correo,contr)
    mensaje = MIMEMultipart()
    mensaje["From"] = correo
    mensaje["To"] = correo
    mensaje["Subject"]="Prueba correo mime"

    html = """
    <html>
    <body>
        <h1 style="color:blue">Esto es un correo con html</h1>
        <p>Estoy utilizando etiquetas para elaborar el body</p>
    </body>
    </html>
    """
    mensaje_html = MIMEText(html,'html')
    mensaje.attach(mensaje_html)
    conec.sendmail(correo,correo,mensaje.as_string())
    print("Correo enviado exitosamente")  
except smtplib.SMTPException as e:
    print(f"Error al mandar el correo {e}")
finally:
    conec.quit()
