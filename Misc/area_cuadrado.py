# Este programa calcula el área de un cuadrado dado uno de sus lados
while True:
    try: 
        lado = int(input('Introduce un lado del cuadrado: '))
        break
    except: 'Eso no es un número'
unidad = input('Introduce la unidad (mm/cm/m): ')
print('El área es de',lado*lado,unidad,'cuadrados')