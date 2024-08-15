class persona():

    def __init__(self):
        self.local = "San Miguel"

    def datos(self,altura,peso):
        self.altura = altura
        self.peso = peso

    def verd(self):
        print(f"La persona de altura {self.altura}"+
               f"y peso {self.peso} es de {self.local}")
        
persona1 = persona()
persona1.datos(1.68,70)
persona1.verd()