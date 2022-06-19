def valormaximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo: maximo = i
    return maximo
print(valormaximo([1,2,3,35,41,2313,523,42,341,5234,234]))

def maxypos(lista):
    maximo = [lista[0],0]
    for i in range(len(lista)):
        if lista[i] > maximo[0]:
            maximo[0] = lista[i]
            maximo[1] = i
    return maximo
print(maxypos([1,2,3,35,41,2313,523,42,341,5234,234]))