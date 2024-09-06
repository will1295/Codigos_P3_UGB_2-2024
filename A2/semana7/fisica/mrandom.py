#import random
from random import random,randrange,choice,choices,shuffle,sample

print(random())

        #(inicio,fin,opcional salto)
print(randrange(0,10,2))
print(randrange(0,10))
print(randrange(20))

lista = ["agua","cafe","jugo","gaseosa"]
print(choice(lista))
print(choices(lista,k=2))

lista2 = [2,65,8,2,8,1,4,8,1]
shuffle(lista2)
print(lista2)

print(sample(lista2,1))
