import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


servidor = ""
puerto = ""
correo = ""
contra = "g"
try: 
    conex = smtplib.SMTP(servidor,puerto)
    conex.starttls()
    conex.login(correo,contra)
    mensaje = MIMEMultipart()
    mensaje["From"] = correo
    mensaje["To"] = correo
    mensaje["Subject"] = "Asunto del mensaje"
    body = "Este correo ha sido generado usando python"
    mensaje.attach(MIMEText(body))
    conex.sendmail(correo,correo,mensaje.as_string())
    print("Corre enviado correctamente")
except smtplib.SMTPResponseException as e: 
    print(f"Hay un error: {e}")
finally:
    conex.quit()
