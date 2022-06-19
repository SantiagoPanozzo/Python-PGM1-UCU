 # Escribir un programa que permite realizar una estadística de los Nombres que llevan los recién nacidos. El programa deberá llevar
 # registro de cada Nombre y la cantidad de niños/niñas que lo llevan (solo primer Nombre).  Para eso solicitará al usuario que ingrese
 # los Nombres por pantalla uno a la vez. Para finalizar, ingresa la cadena vacía y el programa muestra una lista con los Nombres y la
 # cantidad de niños con ese Nombre.

Nombre = 'foo'
tupla = dict() #no es una tupla, solo se llama tupla
print('A continuación introduzca los Nombres uno por uno, deje el espacio vacio para terminar')
while Nombre != '':
    Nombre = input('> ').title()
    if Nombre == '':
        continue
    if Nombre not in tupla:
        tupla[Nombre] = 1
    else: tupla[Nombre] += 1
for Nombres in tupla: 
    print(f'{Nombres:20} | {tupla[Nombres]}') 