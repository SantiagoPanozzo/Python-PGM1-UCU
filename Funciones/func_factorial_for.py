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
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac
n = leer('Introduce un número para calcular su factorial: ')
factorial = fact(n)
print(f'El factorial del número {n} es {factorial}')

print(f'El factorial del número {n} es {math.factorial(n)}')