def maximacadena(lista):
    maxima = lista[0]
    maximas = list()
    for i in lista:
        if len(i) > len(maxima):
            maximas = []
            maxima = i
print(maximacadena(['Pepe','Juan','Maria','Ana']))