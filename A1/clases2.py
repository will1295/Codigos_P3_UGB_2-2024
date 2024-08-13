class libro():

    def __init__(self,titl,aut,edic):
        self.titulo=titl
        self.autor=aut
        self.edicion=edic
        self.editorial = "Libreria El Salvador"

    def datos(self):
        print(f"Titulo: {self.titulo} Autor: {self.autor}, {self.editorial}")

libro1 = libro("La illiada","Homero","Primera edicion")
libro1.datos()

