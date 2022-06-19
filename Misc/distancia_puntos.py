# Programa para calcular la distancia entre dos puntos en un eje
while True:
    try:
        A = int(input('Posición en el eje del primer punto: '))
        break
    except:
        print('Eso no es un número')
while True:
    try:
        B = int(input('Posición en el eje del segundo punto: '))
        break
    except:
        print('Eso no es un número')
dist = abs(A-B)
print('La distancia entre los puntos es de',dist,'unidades')