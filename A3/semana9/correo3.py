import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


servidor = ""
puerto = ""
correo = ""
contra = ""
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
    conex.sendmail(correo,correo,mensaje.as_string())
    print("Corre enviado correctamente")
except smtplib.SMTPResponseException as e: 
    print(f"Hay un error: {e}")
finally:
    conex.quit()
