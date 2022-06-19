# Leer un número y almacenarlo en la variable "n", si el usuario no escribe un número valido se vuelve a pedir el número
while True:
        try:
            n = int(input('Introduce el número a evaluar: '))
            break
        except:
            print('Por favor introduce un número válido')
# Creo una lista para que se vayan guardando las transformaciones para que el usuario las vea
lista_de_transforamaciones = list()
# Funcion para realizar las transformaciones
def transformar():
    global n
    if n%2 != 0:
        n *= 3
        n += 1
    else:
        n /= 2
    lista_de_transforamaciones.append(str(int(n)))
# Variable "veces" como contador de la cantidad de transformaciones de "n"
veces = 0
# Repetimos la funcion hasta que "n" llegue a 1
while n != 1:
    transformar()
    veces += 1
print('\nEl número',int(n),'debe atravesar ',veces,'transformaciones hasta llegar a 1')
ver = input('¿Desea ver las transformaciones? (Si/S/No/N)')
if ver == 'si' or ver == 'Si' or ver == 'S' or ver == 's':
    print(' > '.join(lista_de_transforamaciones))