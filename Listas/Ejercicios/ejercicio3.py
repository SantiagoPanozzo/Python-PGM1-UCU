## Escribir una función que tome una lista de cadenas de caracteres y una cadena adicional como parámetro y
## devuelva True si la cadena está en lista o False sino.
lista1 = list()
lista2 = list()
while True:
    x = input('l1> ')
    if x != '': lista1.append(x)
    else: break
while True:
    x = input('l2> ')
    if x != '': lista2.append(x)
    else: break
for i in lista1:
    for j in lista2:
        if i == j: print(f'{i}: True')
