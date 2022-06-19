def maximadiferencia(lista):
    if len(lista) > 1: mayor = abs(lista[0]-lista[1])
    else: return -1
    maximo = abs(lista[0]-lista[1])
    for i in range(len(lista)-1):
        if abs(lista[i]-lista[i+1]) > maximo: maximo = abs(lista[i]-lista[i+1])
    return maximo
print(maximadiferencia([1, 10, 2, 6, 2, 0]))