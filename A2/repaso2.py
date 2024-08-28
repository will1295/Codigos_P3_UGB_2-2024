"""
Un aeropuerto tiene varias aerolíneas que aterrizan en la pista.
Cada aerolínea tiene cierta cantidad de aviones cada uno con su
respectiva identificación y la persona encargada de hacer esta
tarea necesita un ssitema que registre los aviones que llegan

*También la persona necesita un sistema del itinerario de vuelo
de los aviones.
"""

class Avion():
    def __init__(self,tipo,modelo):
        self.tipo=tipo
        self.modelo=modelo

    def __str__(self):
        return(f"Tipo: {self.tipo}\n"
              f"Modelo: {self.modelo}")

    #def mostrar(self):
    #    print("***Datos***\n"
    #          f"Tipo: {self.tipo}\n"
    #          f"Modelo: {self.modelo}")

class Aerolinea():
    def __init__(self,nombre):
        self.nombre=nombre
        self.aviones=[]

    def agregar(self,avion):
        self.aviones.append(avion)

    def mostrar(self):
        #print(self.aviones)
        print("***Datos de los aviones***")
        print({self.nombre})
        for avion in self.aviones:
            print(avion)


#aerol = Aerolinea("Aerolínea El Salvador")
#avion = Avion("Comercial","Modelo 1234")
#aerol.agregar(avion)
#aerol.mostrar()

naerol=input("Bievenido, ingrese el nombre de la aerolínea: ")
aerol = Aerolinea(naerol)
while True:
    tavion=input("Ingrese el tipo del avión: ")
    mavion=input("Ingrese el modelo del avión: ")
    avion = Avion(tavion,mavion)
    aerol.agregar(avion)
    op = input("¿Desea ingresar otro avión? (s/n)")
    if(op.lower()=='n'):
        aerol.mostrar()
        break
    else:
        continue
    

   