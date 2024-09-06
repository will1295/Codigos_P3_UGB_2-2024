#import datetime
from datetime import datetime

#print(datetime.now())
fecha = datetime.now()
print(fecha)

fecha.day
fecha.month
fecha.year
fecha.hour
fecha.minute
fecha.second

print(fecha.day)

if(fecha.month==9):
    print("Estamos en septiembre!")


print(fecha.strftime("%A"))