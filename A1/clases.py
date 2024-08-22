class carro():
    def __init__(self,color,marca,modelo,vin,
              nmotor,placa,clase,trm):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.vin = vin
        
        self.nmotor = nmotor
        self.placa = placa
        self.clase = clase
        self.trm = trm

        print(f"Datos del vehiculo \n"+
              f"Color: {self.color}\n"+
              f"Marca: {self.marca}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Numero de vin: {self.vin}\n"+
              f"Numero de motor: {self.nmotor}\n"+
              f"Placa: {self.placa}\n"+
              f"Clase: {self.clase}\n"+
              f"Transmision: {self.trm}\n")
    
    def encender(self):
        if(self.trm=="Manual"):
            while True:
                estado = input("¿El carro esta en Neutro? (S/N)")
                if(estado=="S"):
                    print("Se ha dado vuelta a la llave")
                    print("El carro ha encendido")
                    break
                else:
                    print("Se ha dado vuelta a la llave")
                    print("El carro no enciende")
                    continue
        else:
            while True:
                estado = input("¿El carro esta en Parking? (S/N)")
                if(estado=="S"):
                    print("Se ha dado vuelta a la llave")
                    print("El carro ha encendido")
                    break
                else:
                    print("Se ha dado vuelta a la llave")
                    print("El carro no enciende")
                    continue

    def acelerar(self):
        if(self.trm=="Manual"):
            print("Se ha utilizado el clutch")
            print("Se ha cambiado a primera velocidad")
            print("Se ha soltado el clutch despacio")
            print("Se ha utilizado el acelerador")
            print("El carro se ha puesto en marcha")
        else:
            print("Se ha utilizado el freno")
            print("Se ha cambiado a velocidad")
            print("Se ha utilizado el acelerador")
            print("El carro se ha puesto en marcha")


    def cambio(self):
        pass 
        
     

    def frenar(self):
        pass 

    """
    def datos(self,color,marca,modelo,vin,
              nmotor,placa,clase):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.vin = vin
        self.nmotor = nmotor
        self.placa = placa
        self.clase = clase

        print(f"Datos del vehiculo \n"+
              f"Color: {color}\n"+
              f"Marca: {marca}\n"+
              f"Modelo: {modelo}\n"+
              f"Numero de vin: {vin}\n"+
              f"Numero de motor: {nmotor}\n"+
              f"Placa: {placa}\n"+
              f"Clase: {clase}\n")
              """
        
carro1 = carro("Blanco","Toyota","Supra","98KJKJ89","UIR89LK",
              "P21554","Automovil","Manual")
carro1.encender()
carro1.acelerar()
#carro1.datos("Blanco","Toyota","Supra","98KJKJ89","UIR89LK",
#             "P21554","Automovil")
