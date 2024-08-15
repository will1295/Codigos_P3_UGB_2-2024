class Carro():

    #Constructor de clase
    def __init__(self,color,modelo,year,cilindro,hp,trm):
        self.color = color
        self.modelo = modelo
        self.year = year
        self.cilindro = cilindro
        self.hp = hp
        self.trm = trm
        

    """
    #Propiedades
    color = ""
    modelo = ""
    year = ""
    cilindro = ""
    hp = ""

    #Metodos
    def insd(self,color,modelo,year,cilindro,hp):
        self.color = color
        self.modelo = modelo
        self.year = year
        self.cilindro = cilindro
        self.hp = hp
    """

    def mostrard(self):
        print("***Datos del vehículo***\n"+
              f"Color: {self.color}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Año: {self.year}\n"+
              f"Cantidad de cilindros: {self.cilindro}\n"+
              f"Caballos de fuerza: {self.hp}\n"+
              f"Transmision: {self.trm}\n")

    def arrancar(self):
        if(self.trm=="Manual"):
            while True:
                palanca = input("¿La palanca está en Neutro? (S/N)")
                if(palanca=="S"):
                    print("Se ha utilizado la llave y se gira")
                    print("El carro se ha encendido")
                    print("Se ha utilizado el clutch")
                    print("Se cambia a primera")
                    print("Se suelta el clutch despacio")
                    print("Se mete el acelerador")
                    print("Se ha puesto en marcha el carro")
                    break
                else:
                    print("La palanca debe estar en neutro")
                    continue
        else:
            while True:
                caja = input("¿La caja está en Parking? (S/N)")
                if(caja=="S"):
                    print("Se ha utilizado la llave y se gira")
                    print("El carro se ha encendido")
                    print("Se ha utilizado el freno")
                    print("Se cambia a D")
                    print("Se mete el acelerador")
                    print("Se ha puesto en marcha el carro")
                    break
                else:
                    print("La palanca debe estar en Parking")
                    continue
            
    
    def acelerar(self):
        if(self.trm=="Manual"):
            veloc = input("¿En que velocidad va el carro?")
            if(veloc=="1"):
                print("Se ha utilizado el clutch")
                print("Se ha cambiado de primera a segunda")
                print("Se suelta el clutch despacio")
                print("Se mete el acelerador")
                print("El carro ha acelerado")
            elif(veloc=="2"):
                print("Se ha utilizado el clutch")
                print("Se ha cambiado de segunda a tercera")
                print("Se suelta el clutch despacio")
                print("Se mete el acelerador")
                print("El carro ha acelerado")       
        else:
            print("Se ha utilizado el acelerador")
            print("El carro ha acelerado")

    def transportar(self):
        pass


    def retroceder(self):
        pass

    def girar(self,giro):
        if(giro=="Izquierda"):
            print("El carro ha girado hacia la izquierda")
        else:
            print("El carro ha girado hacia la derecha")
        

        
#carro1 = Carro()
#carro1.insd("Rojo anaranjado","Ford Escape",2011,
#            4,200)
#carro1.mostrard()

carro2 = Carro("Azul","Nissan Versa",2012,4,105,"Manual")
carro2.mostrard()
carro2.arrancar()
carro2.acelerar()
carro2.girar("Izquierda")