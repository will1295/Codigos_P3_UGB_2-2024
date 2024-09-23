import smtplib

server = "smtp.gmail.com"
puerto = 587
correo = "monteswillian12@gmail.com"
contra = "hnit bwkd efuw jqmz"
conex = smtplib.SMTP(server,puerto)
#print(conex.ehlo())
conex.starttls()
conex.login(correo,contra)
conex.sendmail(correo,correo,"Subject: Asunto del"+
               "mensaje\n\n Este es el cuerpo")
conex.quit()