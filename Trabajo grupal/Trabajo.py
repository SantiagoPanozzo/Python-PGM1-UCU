import random, os

vac = '⬛' # espacios vacios
oc = '⬜' # espacios con enemigos
cantidad_deseada = 0 # cantidad de enemigos deseada por el usuario
enemigos = cantidad_deseada # cantidad de enemigos variable
disparos = 0 # cantidad de disparos

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
        for i in range (dimensiones):
            columnas.append('') # elementos vacios temporales para despues cambiar
        for i in range(len(columnas)):
            columnas[i] = {
                'enemigo': False,
                'testeado': False,
            }
        return columnas
    filas = list()
    for i in range(dimensiones): filas.append(gen_columnas(dimensiones))
    return filas

# FUNCION QUE MUESTRA EL TABLERO
def mostrar_tablero(tablero,enemigos):
    letras = 'ABCDEFGHIJ'
    print('   ',end='')

    # Imprimir las letras de arriba
    for columnas in range(len(tablero)):
        print(letras[columnas],'',end='')
    del columnas
    print()
    i = 1
    for filas in tablero:
        print(f'{i:2d}', end='')
        for columnas in filas:
            if columnas['testeado']:
                if columnas['enemigo']:
                    print(' o',end='')
                else: print(' x',end='')
            print(vac,end='')
        print()
        i += 1
    print(f'Enemigos restantes: {enemigos}, disparos restantes {disparos}')

# FUNCIÓN QUE MUESTRA EL TABLERO PERO MOSTRANDO LA POSICIÓN DE LOS ENEMIGOS
def eye_spy(tablero):
    letras = 'ABCDEFGHIJ'
    print('   ',end='')

    # Imprimir las letras de arriba
    for columnas in range(len(tablero)):
        print(letras[columnas],'',end='')
    del columnas
    print()
    i = 1
    for filas in tablero:
        print(f'{i:2d}', end='')
        for columnas in filas:
            if columnas['testeado']:
                if columnas['enemigo']:
                    print(' o',end='')
                else: print(' x',end='')
            else:
                if columnas['enemigo']:
                    print(oc,end='')
                else: print(vac,end='')
        print()
        i += 1
    print(f'Enemigos restantes: {enemigos}, disparos restantes {disparos}')

# FUNCIÓN QUE GENERA ENEMIGOS
def gen_enemigos(cantidad_deseada,tablero):
    while cantidad_deseada > 0:
        fila = random.randint(0,len(tablero)-1)
        columna = random.randint(0,len(tablero)-1)
        if not tablero[fila][columna]['enemigo']:
            tablero[fila][columna]['enemigo'] = True
            tablero[fila][columna]['vivo'] = True
            cantidad_deseada -= 1

# FUNCIÓN QUE ESTABLECE LA CANTIDAD DE DISPAROS SEGÚN LA DIFICULTAD
def get_disparos(dimensiones,dificultad):
  dimtotal=dimensiones**2
  if dificultad == 1:
    facil=dimtotal*0.7
    facilint=int(facil)
    if facil-facilint > 0.1:
      facil=(facil-(facil-facilint))+1
    else:
      facil=facil-(facil-facilint)
    return facil
  elif dificultad == 2:
    intermedio=dimtotal*0.5
    intermedioint=int(intermedio)
    if intermedio-intermedioint > 0.1:
      intermedio=(intermedio-(intermedio-intermedioint))+1
    else:
      intermedio=intermedio-(intermedio-intermedioint)
    return intermedio

  elif dificultad == 3:
    dificil=dimtotal*0,3
    dificilint=int(dificil)
    if dificil-dificilint > 0.1:
      dificil=(dificil-(dificil-dificilint))+1
    else:
      dificil=dificil-(dificil-dificilint)
    return dificil

# FUNCIÓN PARA DISPARAR
def disparar(tablero,disparos,cantidad_deseada):
    enemigos = cantidad_deseada
    if disparos > 0:
        coord = ''.join(sorted(list(input('Coordenada: '))))
        while len(coord) != 2: # la coordenada del disparo siempre va a estar en el formato Numero-Letra
            print('Error: cantidad invalida de caracteres, vuelve a intentarlo')
            coord = ''.join(sorted(list(input('Coordenada: '))))
        coordsVert = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
        fila = int(coord[0])-1
        columna = coordsVert[(coord[1]).lower()]
        if tablero[fila][columna]['testeado']:
            print('Ya intentaste en esta casilla, prueba otra')
        else:
            if tablero[fila][columna]['enemigo']:
                tablero[fila][columna]['testeado'] = True
                tablero[fila][columna]['vivo'] = False
                enemigos -= 1
                print('GOLPE!')
            else:
                tablero[fila][columna]['testeado'] = True
                print('Fallaste!')
    else: print('No tienes disparos disponibles')
    return enemigos



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
        ## OBTENER INFORMACIÓN PARA GENERAR EL TABLERO
        dim = intinput('Introduce el tamaño del tablero, entre 3 y 10 (ej: "3" genera un tablero de 3x3) \n> ')
        while dim < 3 or dim > 10:
            print('Erorr: esas dimensiones estan fuera del rango aceptado, vuelve a intentarlo')
            dim = intinput('Introduce el tamaño del tablero, entre 3 y 10 (ej: "3" genera un tablero de 3x3) \n> ')
        
        ## OBTENER INFORMACIÓN PARA GENERAR LOS ENEMIGOS
        cantidad_deseada = intinput('Ingresa cantidad de enemigos (no puede ser mayor que los lados del tablero) \n> ')
        while cantidad_deseada > dim:
            print('Erorr: la cantidad de enemigos supera la cantidad aceptada, vuelve a intentarlo')
            cantidad_deseada = intinput('Ingresa cantidad de enemigos (no puede ser mayor que los lados del tablero) \n> ') 

        ## OBTENER INFORMACIÓN DE DIFICULTAD
        dif = 0
        limpiar()
        while dif < 1 or dif > 3:
            print('¿En que dificultad deseas jugar?\n') 
            print('1) Facil')
            print('2) Intermedio')
            print('3) Dificil')
            dif = intinput('Opcion (1/2/3): ')

        tablero = gen_tablero(dim)
        gen_enemigos(cantidad_deseada,tablero)
        disparos = get_disparos(dim,dif)
        enemigos = cantidad_deseada
        while enemigos > 0:
            limpiar()
            mostrar_tablero(tablero,enemigos)
            eye_spy(tablero)
            print('Disparar')
            enemigos = disparar(tablero,disparos,enemigos)
            disparos -= 1
        print(f'GANASTE! te sobraron {disparos} disparos!')
        input('Pulsa ENTER para continuar...')
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        exit() 
    else: print('Esa no es una opcion')

