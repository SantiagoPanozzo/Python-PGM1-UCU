# Programa para calcular el promedio de cuatro notas con la ponderación: 25%, 15%, 20%, 40%
while True:
    try:
        parcial1 = int(input('Porcentaje del primer parcial: '))
        break
    except:
        print('Eso no es un número')
while True:
    try:
        parcial2 = int(input('Porcentaje del segundo parcial: '))
        break
    except:
        print('Eso no es un número')
while True:
    try:
        parcial3 = int(input('Porcentaje del tercer parcial: '))
        break
    except:
        print('Eso no es un número')
while True:
    try:
        parcial4 = int(input('Porcentaje del cuarto parcial: '))
        break
    except:
        print('Eso no es un número')
parcial1 *= 0.25
parcial2 *= 0.15
parcial3 *= 0.20
parcial4 *= 0.40
final = parcial1 + parcial2 + parcial3 + parcial4
print('La nota final es de:',final,'%')