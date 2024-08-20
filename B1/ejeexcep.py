class MiExcepcion(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje


def div(num1,num2):
    if(num2==0):
        raise MiExcepcion("No se puede dividir entre cero")

print(div(4,0))

