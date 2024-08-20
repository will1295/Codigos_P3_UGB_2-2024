#import pdb
def double(x):
    #pdb.set_trace()
    #breakpoint()
    return x*2

def cuadrado(x):
    return x**2

val=input("Ingresa un número: ")
print(f"El cuadrado de {val} es {cuadrado(val)}")