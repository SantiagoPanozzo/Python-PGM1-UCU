# Programa para determinar cual es el mayor de dos números
while True:
    try:
        numA = int(input('Primer número: '))
        break
    except:
        print('Introduce un número por favor')

while True:
    try:
        numB = int(input('Segundo número: '))
        break
    except:
        print('Introduce un número por favor')
