import smtplib
#from smtplib import SMTP

servidor = ""
puerto = ""
correo = ""
contra = "g"
conex = smtplib.SMTP(servidor,puerto)
#print(conex.ehlo())
conex.starttls()
conex.login(correo,contra)
conex.sendmail(correo,correo,"Subject: Este es el asunto \n\n"+ 
               "Este es el contenido del correo")
conex.quit()