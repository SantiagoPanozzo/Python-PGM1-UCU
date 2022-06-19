# Programa para que, dados 3 números, si el primero es 0 se calcule la suma de los otros dos, o de lo contrario la resta
lista = list()
n = 0
while n < 3:
    while True:
        try:
            indice = lista.append(int(input('Introduce número: ')))
            break
        except:
            print('Eso no es un número')
    n += 1
    print(n,'de 3')
if lista[0] == 0: print(lista[1]+lista[2])
else: print(lista[1]-lista[2])