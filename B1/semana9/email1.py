import smtplib
#from dotenv import load_dotenv
import os
#load_dotenv()

#Reemplazar variables de entorno con tus valores
servidor = os.getenv('SERVIDOR')
puerto = os.getenv('PUERTO')
correo = os.getenv('CORREO')
contr = os.getenv('CONTRA')

try:
    conec = smtplib.SMTP(servidor,puerto)
    conec.starttls()
    conec.login(correo,contr)
    conec.sendmail(correo,correo,"Subject: Este es el asunto"+
                    "\n\n Esto es otro mensaje")
    print("Correo enviado exitosamente")  
except smtplib.SMTPException as e:
    print(f"Error al mandar el correo {e}")
finally:
    conec.quit()
