class persona():
    def __init__(self,nombre,edad,sexo,altura,peso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def mostrarinf(self):
        return("***Datos***\n"+
              f"Nombre completo: {self.nombre}\n"+
              f"Edad: {self.edad}\n"+
              f"Sexo: {self.sexo}\n"+
              f"Altura: {self.altura}\n"+
              f"Peso: {self.peso}\n")


class empleado():

    def __init__(self,sal):
        self.sal = sal

    def salario(self):
        return(f"Su salario es de {self.sal}")
    def trabajar(self):
        pass

class gerente(persona,empleado):

    def __init__(self, nombre, edad, salario,area,sexo,altura,peso):
        persona.__init__(self,nombre,edad,sexo,altura,peso)
        empleado.__init__(self,salario)
        self.area = area

    def mostrar(self):
        datos = self.mostrarinf()
        salario = self.salario()
        print(f"{datos}Area: {self.area}\n"+
              f"{salario}")

        #print("***Datos del empleado***\n"+
        #      f"Nombre completo: {self.nombre}\n"+
        #      f"Edad: {self.edad}\n"+
        #      f"Salario: {self.salario}\n"+
        #      f"Area: {self.area}\n")
        
#empleado1 = empleado("Juan Perez",40,400)
#print(empleado1.mostrarinf())
gerente1 = gerente("Mario Hernandez",46,800,"Ventas","M","1.78","170LB")
gerente1.mostrar()
    