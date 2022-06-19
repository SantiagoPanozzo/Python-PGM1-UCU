# Programa para calcular el factorial de un número
while True:
    try:
        num = int(input('Ingresa un número: '))
        break
    except:
        print('Eso no es un número')
fact = 1
n = 0
while n < num:
    fact = fact * (num - n)
    n += 1
print(fact)