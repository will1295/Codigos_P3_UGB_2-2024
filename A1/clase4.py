from abc import ABC,abstractmethod

class calculos(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetro(self):
        pass

class rectangulo(calculos):

    def __init__(self,base,ancho,lado):
        self.base = base
        self.ancho = ancho
        self.lado = lado

    @property
    def area(self):
        print(self.ancho*self.base)
    #area = "self.ancho*self.base"
        
    @property
    def perimetro(self):
        print(self.lado*4)

re1 = rectangulo(40,20,5)
re1.area
re1.perimetro
    
