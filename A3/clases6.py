from abc import ABC,abstractmethod
class figuras(ABC):


    #Decorators
    @abstractmethod
    def perimetro():
        pass

    @abstractmethod    
    def area():
        pass

    @property
    @abstractmethod
    def dato():
        pass

class rectangulo(figuras):

    #dato = "esto es un rectangulo"
    @property
    def dato(self):
        print("Esto es un rectangulo")

    def area(self,base,altura):
        print(base*altura)

    def perimetro(self,base,altura):
        print((base*2)+(altura*2))

r1 = rectangulo()
r1.area(20,10)
r1.perimetro(20,10)
r1.dato