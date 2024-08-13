class Animal():
    
    def __init__(self,esp,tam,hab,alm):
        self.especie = esp
        self.size = tam
        self.habt = hab
        self.alim = alm

    def dezpl(self):
        print("El animal se esta desplazando")

    def alimn(self):
        print("El animal se esta alimentando")

class Paloma(Animal):
    
    def __init__(self, esp, tam, hab, alm,sexo,color):
        super().__init__(esp, tam, hab, alm)
        self.sexo = sexo
        self.color = color

    def dezpl(self):
        print("La paloma se esta desplazando")

    def volar(self):
        print("La paloma ha alzado el vuelo")

    def cnido(self):
        pass


paloma1 = Paloma("Ala Blanca","Pequeña","Ciudad",
                 "Omnivora","Hembra","Negra y blanca")

paloma1.dezpl()
paloma1.volar()