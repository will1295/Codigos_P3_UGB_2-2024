"""
Un aeropuerto tiene varias aerolineas que aterrizan en la pista,
cada aerolinea tiene cierta cantidad de aviones cada con su
respectiva identificación.
La persona encargada necesita un sistema que le ayude a registrar
los aviones que llegan.

*También sería deseado que el sistema tenga para mostrar
el itinerario de los vuelos.
"""

class Avion():
    def __init__(self,modelo,tipo):
        self.modelo=modelo
        self.tipo=tipo

    def __str__(self):
        return (f"Modelo {self.modelo}\n"+
                f"Tipo {self.tipo}\n")


class Aerolinea():
    def __init__(self,nombre):
        self.nombre=nombre
        self.aviones=[]
        #self.aviones=""

    def reg_avion(self,avion):
        #self.aviones=avion
        self.aviones.append(avion)

    def mostrar(self):
        #print(self.aviones)
        print("***Listado de aviones***")
        for a in self.aviones:
            print(a)


#aerol = Aerolinea("Aerolinea El Salvador")
#avion1 = Avion("Modelo X34","Comercial")
#aerol.reg_avion(avion1)
#aerol.mostrar()

aerol = input("Ingrese el nombre de la aerolínea: ")
aer = Aerolinea(aerol)
while True:
    modav= input("Ingrese el modelo del avión: ")
    modti= input("Ingrese el tipo del avión: ")
    avion1 = Avion(modav,modti)
    aer.reg_avion(avion1)
    op= input("¿Desea registrar otro avión? (s/n): ")
    if(op=="n"):
        aer.mostrar()
        break
    else:
        continue

    