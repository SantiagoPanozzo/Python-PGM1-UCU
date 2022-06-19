# Definir una función que recibe una cadena de caracteres y cuente la cantidad de ocurrencias de cada letra
# del abecedario (sin distinguir mayúsculas de minúsculas).

# Ejemplo:
# funcion("06/2021: Ejercicios en Python.") 
# --> { "E": 3, "J": 1, "R": 1, ... } 

def contaletras(cadena):
    letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    contador = dict()
    for i in cadena:
        i = i.upper()
        if i in letras:
            if i not in contador: contador[i] = 1
            else: contador[i] += 1
    return contador

print(contaletras('06/2021: Ejercicios en Python.'))