def maximadiferencia(lista):
    maximo = lista[0]
    minimo = lista[0]
    for i in lista:
        if i > maximo: maximo = i
        if i < minimo: minimo = i
    return abs(maximo-minimo)

print(maximadiferencia([1, 10, 2, 6, 2, 0]))