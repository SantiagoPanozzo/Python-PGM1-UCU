# Programa para calcular el volumen de un cilindro
from cmath import pi
while True:
    try:
        altura = int(input('Altura del cilindro: '))
        break
    except:
        print('\nEscribe un número por favor')
while True:
    try:
        radio = int(input('Radio del cilindro: '))
        break
    except:
        print('\nEscribe un número por favor')

unidad = input('Unidad trabajada (ej: mm/cm/m): ')
vol = round(((radio**2)*pi*altura),2)
print('El volumen del cilindro es de ',vol,unidad,' cúbicos.')

