class svivos():
    
    def __init__(self,nc,ncf,fam,ev,ta):
        self.ncomun=nc
        self.ncientf=ncf
        self.familia=fam
        self.evida = ev
        self.talimn=ta

    def respirar(self):
        print("El animal esta respirando")

    def aliment(self,comida):
        return f"se alimenta de: {comida}"

    def reproducirse(self):
        print("El animal se reproduce")

    def desechar(self):
        print("El animal defeca")

class leon(svivos):

    def __init__(self, nc, ncf, fam, ev, ta,peso,color,sexo):
        super().__init__(nc, ncf, fam, ev, ta)
        movi = "Cuadrúpedos"
        self.peso = peso 
        self.color = color
        self.sexo = sexo

    def trepar(self):
        print("El leon ha trepado a un arbol")

    def cazar(self):
        if(self.sexo=="Hembra"):
            print("La leona salió a cazar")
        else:
            print("Los leones no suelen cazar")

    def aliment(self, comida):
       dato=super().aliment(comida)
       print(f"El leon {dato}")

leon1 = leon("León","Panthera Leo","Felins",10,"Carnívoro",
             190,"Café","Hembra")
leon1.respirar()
leon1.cazar()
leon1.aliment("Carne")


   


