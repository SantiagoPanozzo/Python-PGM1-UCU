# Implementar en Python una función que recibe como parámetro una lista de números de cédulas de identidad de
# las personas que fueran vacunadas en un centro de vacunación COVID. Cada vez que aparece una cédula en esa lista,
# significa que se registró una dosis recibida por la persona (es decir, si en la lista una cédula x aparece 2 veces,
# significa que esa persona recibió dos dosis). La función debe construir un diccionario en el que, para cada cédula,
# almacene la cantidad de dosis recibidas y devolver una lista de los números de cédula que han recibido 3 o más dosis.

def dosis(lista:list):
    dicc = dict()
    for cedulas in lista:
        if cedulas not in dicc: dicc[cedulas] = 1
        else: dicc[cedulas] += 1
    return [x for x in dicc if dicc[x] >= 3]

print(dosis([1,2,2,3,3,3,4,4,4,4,"1","2","2","3","3","3","4","4","4","4"]))