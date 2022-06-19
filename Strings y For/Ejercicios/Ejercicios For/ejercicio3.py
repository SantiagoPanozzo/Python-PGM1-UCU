## Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar,
## mostrar la sumatoria de los números negativos y el promedio de los positivos. No olvides que no es posible dividir por cero,
## por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
def intinput(mesg):
    while True:
        try: return int(input(mesg))
        except: print('Error: valor no número entero, vuelve a intentarlo')
positivos = 0
poscont = 0
negativos = 0
for i in range(6):
    x = intinput('> ')
    if x < 0:
        negativos += x
    elif x > 0:
        positivos += x
        poscont += 1
if poscont > 0:
    promedio = positivos/poscont
else: promedio = 'ninguno'
print(f'''
Sumatoria de negativos: {negativos}
Promedio de positivos: {promedio}
''')