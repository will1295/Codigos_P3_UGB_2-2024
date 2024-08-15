class carro():

    """
    def datos(self,color,modelo,crines,tmotor,transm):
        self.color = color
        self.modelo = modelo
        self.crines = crines
        self.tmotor = tmotor
        self.transmision= transm
    """
    #Constructor de la clase
    def __init__(self,color,modelo,crines,tmotor,transm):
        self.color = color
        self.modelo = modelo
        self.crines = crines
        self.tmotor = tmotor
        self.transmision= transm

    def mostrard(self):
        print("***Datos del carro***\n"+
              f"Color: {self.color}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Color de los rines: {self.crines}\n"+
              f"Tipo de motor: {self.tmotor}\n"+
              f"Transmisión: {self.transmision}\n")

    def encender(self):
        if(self.transmision=="Manual"):
            print("Se ha introducido la llave")
            while True:
                estado = input("¿La palanca está en neutro? (s/n)")
                if(estado=="s"):
                    
                    print("Se ha girado la llave")
                    print("El motor ha encendido")
                    break
                else:
                    print("El motor no enciende")
                    continue
        else:
            print("Se ha introducido la llave")
            while True:
                estado = input("¿La caja esta en parking? (s/n)")
                if(estado=="s"):
                    
                    print("Se ha girado la llave")
                    print("El motor ha encendido")
                    break
                else:
                    print("El motor no enciende")
                    continue
    
    def enmarcha(self):
        if(self.transmision=="Manual"):
            print("Se mantiene el clutch")
            print("Se cambia a primera velocidad")
            print("Se va liberando el clutch")
            estado = input("Se ha liberado correctamente? (s/n)")
            if(estado == "s"):
                 print("Se utiliza el acelerador")
                 print("El carro se ha puesto en marcha")
            else:
                print("El carro se apagó")
                #self.encender()
        else:
            print("Se mantiene el freno")
            print("Se cambia a D")
            print("Se suelta el freno")
            print("Se utiliza el acelerador")
            print("Se ha puesto en marcha")


    def retroceder():
        pass

    def girar():
        pass

    def pitar():
        pass

#carro1 = carro()
#carro1.datos("Rojo","Hilux","Negro","Gasolina","Manual")
#carro1.mostrard()

carro1 = carro("Rojo","Hilux","Negro","Gasolina","Manual")
#carro1.mostrard()
carro1.encender()
carro1.enmarcha()
carro2 = carro("Azul","Corolla","Gris","Gasolina","Automático")
#carro2.mostrard()