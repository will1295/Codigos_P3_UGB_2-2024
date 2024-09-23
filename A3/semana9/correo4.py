import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

servidor = ""
puerto = ""
correo = ""
contra = ""
#archivo = "archivo.pdf"
archivo = "correo1.py"

try: 
    conex = smtplib.SMTP(servidor,puerto)
    conex.starttls()
    conex.login(correo,contra)
    mensaje = MIMEMultipart()
    mensaje["From"] = correo
    mensaje["To"] = correo
    mensaje["Subject"] = "Asunto del mensaje"
    html = """
    <html>
        <body>
            <h1 style="color:blue">Este es el titulo del mensaje</h1>
            <p style="color:green">Contenido de mi mensaje aqui</p>
        </body>
    </html>
    """
    mensaje.attach(MIMEText(html,'html'))

    with open(archivo,"rb") as adjunto:
        archadj = MIMEBase("application","py")
        archadj.set_payload(adjunto.read())

    encode_base64(archadj)
    archadj.add_header(
        "Content-disposition",
        f"attachment; filename={archivo}"
    )
    mensaje.attach(archadj)

    conex.sendmail(correo,correo,mensaje.as_string())
    print("Corre enviado correctamente")
except smtplib.SMTPResponseException as e: 
    print(f"Hay un error: {e}")
finally:
    conex.quit()
