import datetime

fecha_act = datetime.datetime.now()

fecha_act.day
fecha_act.month
fecha_act.year
fecha_act.hour
fecha_act.minute
fecha_act.second

#print(f"Hoy es {fecha_act.day} de Septiembre")
print(f"Hoy es {fecha_act.day} de {fecha_act.strftime("%B")}")

print(f"Hoy es  {fecha_act.strftime("%A")} {fecha_act.day} de Septiembre")