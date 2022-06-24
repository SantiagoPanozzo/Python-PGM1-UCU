import random, os

vac = '⬛' # espacios vacios
oc = '⬜' # espacios con enemigos
cantidad = 0 # cantidad de enemigos deseada por el usuario
disparos = 0 # cantidad de disparos
enemigos = cantidad # cantidad de enemigos restantes

##########################
#### FUNCIONES UTILES ####
##########################

# FUNCION PARA FORZAR LEER UN NUMERO ENTERO
def intinput(mesg):
    while True:
        try: return(int(input(mesg)))
        except: print("Error: no ingresaste un numero, vuelve a intentarlo")

# FUNCION PARA LIMPIAR LA PANTALLA DEPENDIENDO DEL SISTEMA OPERATIVO
def limpiar():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

##############################
#### FUNCIONES DEL JUEGO #####
##############################

# FUNCION QUE GENERA EL TABLERO
def gen_tablero(dimensiones):
    def gen_columnas(dimensiones):
        columnas = list()
        for i in range (dimensiones): # sumamos 2, 1 por el rango y 1 porque no vamos a tomar el elemento 0 por comodidad
            columnas.append('') # elementos vacios temporales para despues cambiar
        for i in range(len(columnas)):
            if i == 0:
                continue
            columnas[i] = {
                'enemigo': False,
                'testeado': False,
            }
        return columnas
    filas = list()
    for i in range(dimensiones): filas.append(gen_columnas(dimensiones))
    return filas

# FUNCION QUE MUESTRA EL TABLERO
def mostrar_tablero(tablero):
    letras = 'ABCDEFGHIJ'
    print('   ',end='')

    # Imprimir las letras de arriba
    for columnas in range(len(tablero)):
        print(letras[columnas],'',end='')
    print()
    i = 1
    for filas in tablero:
        print(f'{i:2d}', end='')
        for columnas in filas:
            if columnas['test']:
                if columnas['enemigo']:
                    print(' o',end='')
                else: print(' x',end='')
            print(vac,end='')
        print()
        i += 1
    print(f'Enemigos restantes: {enemigos}, disparos restantes {disparos}')

############################
##### MENU Y EJECUCION #####
############################

while True:
    limpiar()
    x = intinput('''
¿Qué deseas hacer?

1) Jugar
2) Instrucciones
3) Reglas
4) Salir

Opcion (1/2/3/4): ''')
    if x == 1:
        tablero = gen_tablero(5)
        mostrar_tablero(tablero)
        input()

    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        exit() 
    else: print('Esa no es una opcion')

