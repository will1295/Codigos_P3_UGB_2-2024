#import random
from random import choices,randrange,shuffle,sample
#random.seed(10)
#print(random.random())
#print(random.random())

lista = ["manzanas","peras","uvas","naranjas"]
print(choices(lista))

print(randrange(1,10))

shuffle(lista)
print(lista)

print(sample(lista,2))