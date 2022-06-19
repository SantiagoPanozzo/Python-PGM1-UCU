pares, impares = 0, 0
seguir = True
while seguir == True:
    num = int(input('Ingresa un número positivo (o 0 para terminar): '))
    if num == 0:
        print(f'Se ingresaron {pares} números pares y {impares} números impares')
        seguir = False
    while num < 0:
        print('Por favor, ingresa un número positivo')
        num = int(input('Ingresa un número positivo (o 0 para terminar): '))
    if num%2 == 0:
        pares += 1
    else:
        impares += 1