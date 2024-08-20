class Padre():
    atributo1="Valor1"
    atributo2="Valor2"
    atributo3="Valor3"

    def metodo1(self):
        self.atributo4="Valor4"
        print("Este método es del padre")

    def metodo2(self):
        pass

    def metodo3(self):
        pass

class Hija(Padre):
    atributoh="atributo de la hija"
    atributoh2="otro atributo"

    def metodoh(self):
        pass

hija1 = Hija()
print(hija1.atributo1)
hija1.metodo1()
print(hija1.atributo4)