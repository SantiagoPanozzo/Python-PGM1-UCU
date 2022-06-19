print('Este programa reproducirá la sucesión de Fibonacci hasta el último número menor al que usted ingrese')
while True:
    try:
        num = int(input('Número: '))
        break
    except: print('Introduce un número por favor')
a = 0
b = 1
print (a)
print (b)
while b < num and a < num:
    a += b
    if a < num:
        print(a)
    b += a
    if b < num:
        print(b)