# Programa para determinar cual es el mayor de 3 números
while True:
    try:
        A = int(input('Primer número: '))
        break
    except:
        print('Eso no es un número')
while True:
    try:
        B = int(input('Segundo número: '))
        break
    except:
        print('Eso no es un número')
while True:
    try:
        C = int(input('Tercer número: '))
        break
    except:

        print('Eso no es un número')

if A != B:
    if A > B: mayor = A
    else: mayor = B
if mayor != C:
    if mayor < C: mayor = C
print('El mayor es',mayor)
