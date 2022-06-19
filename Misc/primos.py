# Programa para saber cuantos números primos hay en una cantidad de números dada
n = 0
while True:
    try: 
        cantidad = int(input('Introduce la cantidad de números a evaluar: '))
        break
    except:
        print('Eso no es un número')
n_primos = 0
n_noprimos = 0
while n < cantidad:
    m = 1
    while True:
        try: 
            num = int(input('Introduce un número: '))
            break
        except: print('Eso no es un número')
    noesprimo = False
    while m < num:
        cuenta = num%m
        if m != 1 and m != num and cuenta == 0:
            noesprimo = True
        m = m+1
    if noesprimo == True:
        n_noprimos += 1
    else: n_primos += 1
    n = n + 1
print('Hay',n_primos,'primos')
print('Hay',n_noprimos,'no primos')