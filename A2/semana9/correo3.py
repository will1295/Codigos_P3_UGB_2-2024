import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
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
    mensaje["Subject"] = "Probando envio de adjunto"

    html = """
    <html>
        <body>
            <h1 style="color:blue">SMTPLIB</h1>
            <p style="color:red">Estoy mandando un archivo adjunto</p>
        </body>
    </html>
    """
    mhtml = MIMEText(html,'html')
    mensaje.attach(mhtml)

    archivo = "archivo.pdf"
    with open(archivo,"rb") as adjunto:
        archad = MIMEBase("application","pdf")
        archad.set_payload(adjunto.read())
    
    encode_base64(archad)
    archad.add_header(
        "Content-Disposition",
        f"attachment;filename={archivo}",
    )

    mensaje.attach(archad)


    conex.sendmail(correo,correo,mensaje.as_string())
    conex.quit()
    print("El correo se ha enviado correctamente")
except smtplib.SMTPResponseException as e:
    print(f"Se ha encontrado un error: {e}")
