import random
from random import randint

def lista_gen():
    lista = list()
    for x in range(30):
        lista.append(randint(0,9))
    return lista

lista1 = lista_gen()
lista2 = lista_gen()
lista3 = list()
for i in range(len(lista1)):
    if lista1[i] == lista2[i]:
        lista3.append(i)
print(f'{lista1}\n{lista2}\n{lista3}')