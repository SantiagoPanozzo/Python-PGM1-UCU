import os

def menu():
    return('''
Seleccione una opción:
A: Agregar elemento al conjunto
B: Borrar elemento del conjunto
T: Borrar todos los elementos del conjunto
M: Mostrar conjunto
F: Finalizar''')

def floatinput(mesg):
    while True:
        try: return(str(float(input(mesg))))
        except: print('Error: No es un número, vuelve a intentarlo')

def main(conjunto):
    opciones = 'aAbBtTmMfF'
    opcion = input('Opción: ')
    while opcion not in opciones:
        print('Opcion no reconocida, vuelve a intentarlo')
        opcion = input('Opción: ')
    if opcion == ('a' or 'A'):
        print('Ingresa el numero a agregar al conjunto y pulsa ENTER:')
        x = floatinput('> ')
        if x not in conjunto:
            conjunto.add(x)
            print(f'{x} añadido al conjunto')
        else: print('Ese número ya fue agregado')
    if opcion == ('b' or 'B'):
        print('Ingresa el numero a eliminar del conjunto y pulsa ENTER:')
        x = floatinput('> ')
        if x in conjunto:
            conjunto.remove(x)
            print(f'Eliminado del conjunto {x}')
        else: print('Ese número no se encuentra en el conjunto')
    if opcion == ('t' or 'T'):
        if len(conjunto) > 0:
            for x in [x for x in conjunto]:
                conjunto.remove(x)
            print('Eliminados todos los elementos del conjunto')
        else: print('El conjunto ya está vacío')
    if opcion == ('m' or 'M'):
        if len(conjunto) > 0: print(', '.join(conjunto))
        else: print('Conjunto vacío')
    if opcion == ('f' or 'F'):
        return False
    input('Pulsa ENTER para continuar...')
    return True

activacion = True
numeros = set()
while activacion == True:
    # limpiar pantalla, el comando depende del sistema
    if os.name == 'nt': os.system('cls')
    else: os.system(clear)
    print(menu())
    activacion = main(numeros)