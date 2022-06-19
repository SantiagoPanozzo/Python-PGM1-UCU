import math
# Funcion para leer número enteros del teclado evitando errores
def leer(mesg):
    while True:
        try:
            x = int(input(mesg))
            return x
        except:
            print('Valor inválido, vuelve a intentarlo')

def fact(n):
    i = 1
    fac = 1
    while i <= n:
        fac *= i
        i += 1
    return fac
n = leer('Introduce un número para calcular su factorial: ')
factorial = fact(n)
print(f'El factorial del número {n} es {factorial}')

print(f'El factorial del número {n} es {math.factorial(n)}')