"""
Un aeropuerto tiene varias aerolíneas que aterrizan en la pista,
cada aerolínea tiene cierta cantidad de aviones cada uno con
su respectiva identificacion. La persona encargada necesita
un sistema que le ayude a registrar los aviones que llegan.

*También seria deseado que se establezca el sistema para el
itinerario de los vuelos de los aviones.

"""

class Avion():
    def __init__(self,modelo,tipo):
        self.modelo=modelo
        #self.aerolinea=aerolinea
        self.tipo=tipo
        #self.listado=[]

    def __str__(self):
        return f"Avion. Modelo: {self.modelo} Tipo: {self.tipo}"
    """
    def mostrar(self):
        #print("***Datos del avión***\n"
        #      f"Modelo del avión: {self.modelo}\n"
        #      f"Aerolínea: {self.aerolinea}\n"
        #      f"Tipo {self.tipo}\n")
        print(self.listado)
        """

class Aerolinea:
    def __init__(self,nombre):
        self.nombre = nombre
        self.aviones = []

    def agregar_av(self,avion):
        self.aviones.append(avion)

    def mostrar(self):
        print("***Listado de aviones***")
        for avion in self.aviones:
            print(avion)
"""
while True:
    modelo = input("Ingrese el modelo del avión: ")
    aerolinea = input("Ingrese la aerolínea: ")
    tipo = input("Ingrese el tipo del avión: ")
    avion = Avion(modelo,aerolinea,tipo)
    #avion.listado.append(avion)
    op = input("¿Desea agregar otro avion? (s/n)")
    if(op == "n"):
        avion.mostrar()
        break
    else:
        continue
"""
aerolinea = input("Ingrese la aerolínea: ")
aerol = Aerolinea(aerolinea)
while True:
    #aerolinea = input("Ingrese la aerolínea: ")
    #aerol = Aerolinea(aerolinea)
    modelo = input("Ingrese el modelo del avión: ")
    tipo = input("Ingrese el tipo del avión: ")
    avi = Avion(modelo,tipo)
    aerol.agregar_av(avi)
    op = input("¿Desea agregar otro avion? (s/n)")
    if(op == "n"):
        aerol.mostrar()
        break
    else:
        continue
    
    
