# Programa para determinar cuantos números positivos, negativos y ceros hay en una secuencia dada
while True:
    try:
        cantidad = int(input('Introduce cuantos números van a ser evaluados: '))
        break
    except:
        print('Eso no es un número valido')
negativos = 0
positivos = 0
ceros = 0
n = 0
while n < cantidad:
    while True:
        try:
            num = int(input('Introduce un número: '))
            break
        except:
            print('Eso no es un número')
    if num < 0:
        negativos += 1
    if num == 0:
        ceros += 1
    if num > 0:
        positivos += 1
    n += 1
print('Hay',negativos,'números negativos')
print('Hay',ceros,'ceros')
print('Hay',positivos,'números positivos')