## Definir una función que permita generar un cartón de lotería. Un cartón de lotería contiene 3 filas con 5 números cada
## una. Los números son aleatorio entre 1 y 99 y no se repiten. La función debe retornar una lista conteniendo las 3 filas,
## es decir 3 listas, con 5 números.

## Ej: generar_carton() -> [[13,10,11,16,15],[1,8,62,36,45],[99,97,85,73,28]]
import random

def generar_carton():
    fila1 = list()
    fila2 = list()
    fila3 = list()
    numeros = (random.sample(range(1,99),15))
    for i in range(0,13,3):
        fila1.append(numeros[i])
        fila2.append(numeros[i+1])
        fila3.append(numeros[i+2])
    return [fila1,fila2,fila3]
print(generar_carton())