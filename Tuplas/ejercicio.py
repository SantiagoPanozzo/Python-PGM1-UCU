# Implemente una función que reciba por parámetro una lista de tuplas, y retorne una tupla de la forma:
# (a1, a2, …, an)
# Donde ai corresponde a la suma de los elementos de las tuplas en la posición i.
# Ejemplo: [(1, 2), (3, 4)] -> (4, 6)
# Puede suponer que todas las tuplas tienen la misma cantidad de elementos.

def tortuga(lista):
    salida = list()
    salida = [0 for i in range(len(lista[0]))]
    for tuplas in lista:
        for elementos in range(len(tuplas)):
            salida[elementos] += tuplas[elementos]
    return tuple(salida)

print(tortuga([(1,2,1,2),(3,4,3,4),(1,2,1,2)]))