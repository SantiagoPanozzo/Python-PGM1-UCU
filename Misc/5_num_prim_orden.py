# Un programa que dados 5 números, el primero marca cual de los otros se debe imprimir
lista = list()
a = 0
while a < 5:
    lista.append(int(input('Introduce un número: ')))
    a += 1
    print(a,'de 5')
print(lista[lista[0]])