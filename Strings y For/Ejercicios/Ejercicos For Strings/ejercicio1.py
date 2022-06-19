## Escriba un programa en Python donde el usuario ingrese un string por teclado y luego imprima todas sus letras
## (una en cada fila). Realíce una versión iterando sobre las letras del string y otra iterando sobre los índices de las
## letras (es decir, usando for-range). Ej: si el string ingresado es auto deberá escribir:
## a
## u
## t
## o
string = input('> ')
if int(input('Version 1/2: ')) == 1:
    for i in string:
        print(i)
else:
    for i in range(len(string)):
        print(string[i])