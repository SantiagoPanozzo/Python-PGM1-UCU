while True:
    try:
        año = int(input('Introduce el año: '))
        break
    except:
        print('Debes introducir un año válido, intentalo de nuevo')
años_transcurridos = 0
ciudad_A, tasa_A = 3500000, 0.07
ciudad_B, tasa_B = 5000000, 0.05
while ciudad_A <= ciudad_B:
    ciudad_A += (ciudad_A * tasa_A)
    ciudad_B += (ciudad_B * tasa_B)
    años_transcurridos += 1
print('Para el año',año+años_transcurridos,'la ciudad A tendrá',int(ciudad_A),'habitantes, superando a la ciudad B con',int(ciudad_B),'habitantes')