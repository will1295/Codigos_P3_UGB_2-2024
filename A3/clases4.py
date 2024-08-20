class empleado():

    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def mostrarinf(self):
        return("***Datos del empleado***\n"+
              f"Nombre completo: {self.nombre}\n"+
              f"Edad: {self.edad}\n"+
              f"Salario: {self.salario}\n")

    def trabajar(self):
        pass

class gerente(empleado):

    def __init__(self, nombre, edad, salario,area):
        super().__init__(nombre, edad, salario)
        self.area = area

    def mostrarinf(self):
        datos = super().mostrarinf()
        print(f"{datos}Area: {self.area}\n")

        #print("***Datos del empleado***\n"+
        #      f"Nombre completo: {self.nombre}\n"+
        #      f"Edad: {self.edad}\n"+
        #      f"Salario: {self.salario}\n"+
        #      f"Area: {self.area}\n")
        
empleado1 = empleado("Juan Perez",40,400)
print(empleado1.mostrarinf())
gerente1 = gerente("Mario Hernandez",46,800,"Ventas")
gerente1.mostrarinf()
    