import pdb
def area(base,altura):
    return base*altura 
try:
    base = input("Escribe el valor de la base: ")
    altura = input("Escribe el valor de la altura: ")
    print(area(base,altura))
except:
    pdb.post_mortem()
