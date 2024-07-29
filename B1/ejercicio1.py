def calculo_velocidad (distancia, tiempo):
	velocidad = distancia/tiempo
	return velocidad

print("Escriba el valor de la distancia: ")
dis = float(input()) 
print("Escriba el valor del tiempo: ")
ti = float(input())
print(calculo_velocidad(dis,ti))


def cal_vel(dis, tim):
  velocidad = dis / tim
  print(f"la velocidad del vehiculo es {velocidad} kilometros por hora km/h")
cal_vel(20,10)


def grupo(*nombres):
     for nombres in nombres:
         print("El grupo esta conformado por: "+nombres)
grupo("Juana","Maria","Pedro","Anita")