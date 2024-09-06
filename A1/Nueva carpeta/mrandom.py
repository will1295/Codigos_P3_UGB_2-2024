#import random
from random import random,randrange,randint,choice,shuffle,sample

print(random())

#print(randrange(0,10))
#print(randint(0,10))

num1 = randrange(0,10,2) #0,2,4,6,8
num2 = randint(0,10)
print(num1)
print(num2)

lista = ["cocacola","agua","te helado","cafe"]
print(choice(lista))

lista2 = [23,5,8,9,1,2,9,6]
shuffle(lista2)
print(lista2)


lista3 = ["zanahorias","lechuga","pepino","repollo"]
print(sample(lista3,2))