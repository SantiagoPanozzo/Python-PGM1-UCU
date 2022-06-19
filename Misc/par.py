# Programa para determinar si un número es par o no
while True:
    try: 
        num = float(input('Introduce un número: '))
        break
    except:
        print('Eso no es un número')
div = num%2
if div == 0:
    print('El número',int(num),'es par')
else:
    print('El número',int(num),'no es par')