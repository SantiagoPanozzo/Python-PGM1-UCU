## Escribir un código que lea por teclado números y los guarde en una lista, el proceso finaliza cuando
## se ingrese un número negativo. Mostrar los números pares.
lista = list()
x = True
while x == True:
    try:
        y = float(input('> '))
        if y < 0:
            break
        else: lista.append(y)
    except: print('Vuelve a intentarlo')
pares = list()
for i in lista:
    if i % 2 == 0:
        pares.append(str(int(i)))
print(f'Pares: {", ".join(pares)}')