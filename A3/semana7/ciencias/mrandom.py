#import random
from random import random,randrange,choice,choices,shuffle,sample

#print(random.random())
print(random())

print(randrange(6))
print(randrange(0,10))
print(randrange(0,10,2))


listado = ["agua","jugo","cafe","gaseosa"]
print(choice(listado))

print(choices(listado,k=2))

lista2 = [1,2,3,4,5,6,7,8]
shuffle(lista2)
print(lista2)

print(sample(lista2,2))