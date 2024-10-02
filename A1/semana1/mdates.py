import datetime

#print(datetime.datetime.now())

nombre = input("Hola, dime tu nombre: ")

fecha = datetime.datetime.now()
print(fecha.hour)

if(fecha.hour<=12):
    print(f"Buenos días{nombre}")
elif(fecha.hour>=12):
    print(f"Buenas tardes{nombre}")
else:
    print("Es la hora del almuerzo")


fecha.hour
fecha.minute
fecha.second
fecha.day
fecha.month
fecha.year
fecha.microsecond

#AAAA:MM:DD HH:MM:SS

#print(fecha.day)
print(fecha.strftime("%A"))