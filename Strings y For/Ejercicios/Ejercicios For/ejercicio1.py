## Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración,
## solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.
def intinput(mesg):
    while True:
        try: return int(input(mesg))
        except: print('Error: valor no número entero, vuelve a intentarlo')
total = 0
for i in range(intinput('Cantidad: ')):
    total += intinput('> ')
print(total)