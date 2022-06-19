'''Escribir una función que reciba como parámetros, una lista con números enteros y otro número entero.
La función debe devolver una nueva lista con todos los números que son mayores al número recibido como parámetro.

Ej: num_mayores([3, 7, 8, 34, 56, 89, 7, 12], 20) --> [34, 56, 89]'''

def num_mayores(lista,may):
    mayores = []
    for i in lista:
        if i > may:
            mayores.append(i)
    return mayores

# Demostracion
print(num_mayores([3, 7, 8, 34, 56, 89, 7, 12, 20], 20))