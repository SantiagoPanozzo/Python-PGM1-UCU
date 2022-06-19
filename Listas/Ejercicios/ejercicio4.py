## Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre
## en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random
lista = list()
for i in range(10):
    lista.append(random.randint(1,10))
print('n , ^2 , ^3\n')
for i in lista:
    print(f'{i}, {i**2}, {i**3}')