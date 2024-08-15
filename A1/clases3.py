class ave():
    
    def __init__(self,cplumas,puedev,habitat):
        alas=2
        self.cplumas=cplumas
        self.puedev = puedev
        self.habitat = habitat 

    def graznar(self):
        print("El ave ha graznado")

    def comer(self,comida):
        return f"come {comida}"

    def descansar(self):
        print(f"El ave esta descansando")

    def phuevos(self):
        print(f"El ave ha puesto un huevo")


class gallina(ave):

    def __init__(self,tipo,tcresta,cplumas,puedev,habitat):
        super().__init__(cplumas,puedev,habitat)
        self.tipo=tipo
        self.tcresta = tcresta

    def datos(self):
        print(f"Tipo de gallina: {self.tipo}"+
              f"Tamaño de cresta: {self.tcresta}"+
              f"Color de plumas: {self.cplumas}"+
              f"Puede volar: {self.puedev}"+
              f"Habitat: {self.habitat}")
   
    #Overriding
    def graznar(self):
        print("La gallina esta cacareando")

    def comer(self, comida):
        #Llamando al metodo comer de la superclase con super()
        frase = super().comer(comida)
        print(f"La gallina {frase}")


gallina1 = gallina("India","Mediana","Negro con anaranjado","No","Granja")
gallina1.datos()
gallina1.graznar()
gallina1.comer("maiz")
gallina1.descansar()