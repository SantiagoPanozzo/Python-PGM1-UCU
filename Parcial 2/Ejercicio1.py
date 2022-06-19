'''Escribir una función que permita determinar si, dada una lista de palabras, todas riman. Para esta función,
 decimos que las palabras riman si las últimas tres letras son iguales. Por ejemplo, las palabras: programación,
 construcción, abstracción y oración, riman entre sí. En ese caso, la función devuelve True. En caso contrario,
 devuelve False.

Ejemplo:

                riman(["lunes", "viernes", "tienes"]) ---> True

               riman(["lunes", "martes", "tienes"]) ---> False'''

def riman(palabras):
    rima = (palabras[0])[-3:]
    for i in palabras:
        fin = i[-3:]
        if fin != rima:
            return False
    return True

print(riman(["lunes", "viernes", "tienes"]))
print(riman(["lunes", "martes", "tienes"]))