    #nombrefun  #parametro
def doblar_valor(numero):
    n2 = numero*2
    return n2
    #valor de retorno
n = 10
     #invocacion
(doblar_valor(n))
                #argumento


def describ(tipom,nombrem):
    print(f"Mi mascota es un {tipom} y se llama {nombrem}")

describ("Perro","Kaiser")
describ("Gato","Pelusa")
describ(nombrem="Samson",tipom="Gato")


def datoes(nombre,carnet,sede="San Miguel"):
    print(f"Datos del estudiante: {nombre} {carnet} {sede}" )

datoes("Juanita Perez","SMSS12345")
datoes("Pedro Sanchez","SMSS4559","Usulutan")


def datosc(*materias):
    print(materias)

datosc("Programacion","Bases de datos","Ingles")
datosc("Programacion","Robotica")
datosc()
