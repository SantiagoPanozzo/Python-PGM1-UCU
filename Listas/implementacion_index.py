def indice(entrada,valor):
    contador = -1
    for i in entrada:
        contador += 1
        if i == valor:
            return(contador)
print(indice(((input('> ').split())),input('> ')))

def myindex(lista,valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i