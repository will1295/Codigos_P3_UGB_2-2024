import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
    mensaje = MIMEMultipart()
    mensaje["From"] = correo
    mensaje["To"] = correo
    mensaje["Subject"] = "Probando mime"

    html = """
    <html>
        <body>
            <h1 style="color:blue">Titulo del correo</h1>
            <p style="color:red">Esto es un parrafo</p>
        </body>
    </html>
    """
    mhtml = MIMEText(html,'html')
    mensaje.attach(mhtml)
    conex.sendmail(correo,correo,mensaje.as_string())
    conex.quit()
    print("El correo se ha enviado correctamente")
except smtplib.SMTPResponseException as e:
    print(f"Se ha encontrado un error: {e}")
