class fcarros:
    marca = "BMW"
    color = ""
    nmotor = ""
    modelo = ""
    year = ""
    transmi=""

    #Constructor de clase
    def __init__(self,color,nmotor,modelo,year,transmi):
         self.color = color
         self.nmotor = nmotor
         self.modelo = modelo
         self.year = year
         self.transmi = transmi
         print("-----------------------------\n"+
              "***Datos del vehículo***\n"+
              f"Marca: {self.marca}\n"+
              f"Color: {self.color}\n"+
              f"Número de motor: {self.nmotor}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Año: {self.year}\n"
              f"Transmisión: {self.transmi}\n")


    """
    def datos(self,marca,color,nmotor,modelo,year):
        print("-----------------------------\n"+
              "***Datos del vehículo***\n"+
              f"Marca: {marca}\n"+
              f"Color: {color}\n"+
              f"Número de motor: {nmotor}\n"+
              f"Modelo: {modelo}\n"+
              f"Año: {year}\n")
    """


    def encender(self):
        print("El carro ha encendido")

    def ponmarcha(self):
        if(self.transmi=="Automatica"):
            while True:
                estado = input("¿El carro está en Parking? (S/N)")
                if(estado=="S"):
                    print("Se ha cambiado a D")
                    print("Se ha utilizado el acelerador")
                    print("El carro se ha puesto en marcha")
                    break
                else:
                    print("El carro no se pone en marcha")
                    continue
        elif(self.transmi =="Manual"):
                while True:
                    estado = input("¿El carro está en Neutro? (S/N)")
                    if(estado=="S"):
                        print("Se ha utilizado el clutch")
                        print("Se ha cambiado a primera velocidad")
                        print("Se ha utilizado el acelerador")
                        print("El carro se ha puesto en marcha")
                        break
                    else:
                        print("El carro no se pone en marcha")
                        continue

    def acelerar(self):
       pass

    def frenar(self):
        pass

    def pitar(self):
        pass

    def derrapar(self):
        pass

    
#carro1 = fcarros("Toyota","Rojo","LKDSAJ1238","Tacoma",3000)
#carro1.datos("Toyota","Rojo","LKDSAJ1238","Tacoma",3000)

#carro2 = fcarros("Nissan","Negro","JKSDAKJ1238","Rogue",2020)
#carro2.datos("Nissan","Negro","JKSDAKJ1238","Rogue",2020)

#carro1 = fcarros("Azul","LBBNAJ1238","SUV",2009,"Automatica")
#carro1.encender()
#carro1.ponmarcha()

carro2 = fcarros("Azul","LBBNAJ1238","SUV",2009,"Manual")
carro2.encender()
carro2.ponmarcha()
