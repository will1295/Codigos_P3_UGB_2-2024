class Persona():

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return(f"Hola {self.nombre} tienes {self.edad} años de edad")

    def datos(self):
        pass

persona1 = Persona("Pedro",20)
print(persona1)