#import pdb
def poten(num1,p):
    total = num1**p
    return total

num = input("Ingresa un número: ")
#pdb.set_trace()
p = int(input("Ingresa la potencia: "))
#breakpoint()
print(poten(num,p))