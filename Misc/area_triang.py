# Programa para calcular el área de un triángulo
while True:
    try:
        base = int(input('Base del triángulo: '))
        break
    except:
        print('\nEscribe un número por favor')
while True:
    try:
        altura = int(input('Altura del triángulo: '))
        break
    except:
        print('\nEscribe un número por favor')

unidad = input('Unidad trabajada (ej: mm/cm/m): ')
area = (altura * base)/2
print('El área del triángulo es de ',area,unidad,' cuadrados.')