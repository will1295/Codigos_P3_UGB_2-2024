class Empleado():

    def __init__(self,sal,jor,sexo,edad,telf):
        self.salario=sal
        self.jornada=jor
        self.sexo=sexo
        self.edad=edad
        self.telf=telf

    def csalario(self):
        pass

    def caguinaldo(self):
        pass

class Gerente(Empleado):

    def __init__(self, sal, jor, sexo, edad, telf,titulo,area):
        super().__init__(sal, jor, sexo, edad, telf)
        self.titulo = titulo
        self.area = area

    def admins(self):
        pass

    def hreportes(self):
        pass

    def csalario(self,horas):
        print(20*horas)

    def caguinaldo(self, ttrabajo):
        print(ttrabajo*(float(salario))*0.10)
 

class Ordenanza(Empleado):
    def __init__(self, sal, jor, sexo, edad, telf,sector):
        super().__init__(sal, jor, sexo, edad, telf)
        self.sector = sector

    def barrer(self):
        pass

    def trapear(self):
        pass

    def csalario(self,horas):
        print(10*horas)

    def caguinaldo(self, ttrabajo):
        print(ttrabajo*super().caguinaldo())

while True:
    print("Bievenido al ingreso de nomina")
    op=input("¿Que tipo de empleado desea ingresar?\n"+
             "1.Gerente\n"+
             "2.Ordenanza\n")
    if(op=="1"):
        salario=input("Ingrese el salario en $: ")
        jorn=input("Jornada laboral: ")
        sexo=input("Sexo (F/M): " )
        edad=input("Ingrese la edad: ")
        telef=input("Ingrese el teléfono: ")
        titulo=input("Ingrese el titulo: ")
        sector=input("Ingrese el sector: ")
        gerente1 = Gerente(salario,jorn,sexo,edad,telef,titulo,sector)
        horas = int(input("Ingrese la cantidad de horas laboradas"))
        gerente1.csalario(horas)
        tiempo = int(input("Ingrese el numero de años laborados"))
        gerente1.caguinaldo(tiempo)