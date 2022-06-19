# Crear una función que permita determinar probabilísticamente resultados que se pueden obtener en una tirada de un dado. Para eso
# se deben generar 10.000 tiradas aleatorias y obtener el porcentaje que resulta para cada número posible en el dado.

# La función debe devolver un diccionario como el siguiente: {1: 10, 2: 24, 3: 26, 4: 19, 5: 11, 6: 10} donde la clave corresponde
# al número de la cara del dado (1 a 6) y el valor al porcentaje de tiradas que salió dicho número (en este caso el 1 salió el 10%
# de las tiradas - 1000 tiradas- ).

# Pueden usar más de un diccionario para la solución.

from random import randint
# abandon all hope ye who try to read this
def dadar():
    dadamientos = {1:0,2:0,3:0,4:0,5:0,6:0}
    for dados in range(10000):
        dadacion = randint(1,6)
        dadamientos[dadacion] += 1
    for dadados in dadamientos:
        dadamientos[dadados] = round((dadamientos[dadados]/10000*100),2)
    return dadamientos

print(dadar())