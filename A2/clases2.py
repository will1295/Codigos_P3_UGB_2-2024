class Padre():
    atributo1="valor"
    atributo2="valor2"
    atributo3="valor3"

    def metodo1(self):
        print("Este metodo es de la clase padre")

    def metodo2(self):
        pass
#Clase hija hereda de padre
class Hija(Padre):
    atributoh="hija"

    def metodoh(self):
        print("Este metodo es de la clase hija")

padre = Padre()
padre.metodo1()
hija = Hija()
hija.metodo1()