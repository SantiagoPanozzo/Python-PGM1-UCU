import random, os

vac = '⬛' # espacios vacios
oc = '⬜' # espacios con enemigos
cantidad_deseada = 0 # cantidad de enemigos deseada por el usuario
enemigos = cantidad_deseada # cantidad de enemigos como contador variable
disparos = 0 # cantidad de disparos
xray = False # si se habilita esta variable, se muestra la posición de los enemigos al jugar

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
        columnas = list() # las columnas son una lista
        for i in range (dimensiones):
            columnas.append('') # elementos vacios temporales
        for i in range(len(columnas)): 
            columnas[i] = { # sustituir los elemntos vacios por dicionarios
                'enemigo': False, # por defecto no hay enemigos en la casilla
                'testeado': False, # por defecto el usuario aún no interactuó con la casilla
            }
        return columnas
    filas = list() # filas es una lista
    for i in range(dimensiones): filas.append(gen_columnas(dimensiones)) # las columnas son una lista de diccionarios dentro de la lista de filas
    return filas

# FUNCION QUE MUESTRA EL TABLERO
def mostrar_tablero(tablero,enemigos):
    letras = 'ABCDEFGHIJ'
    print('   ',end='') # espacio estetico

    # Imprimir las letras de arriba de las columnas
    for columnas in range(len(tablero)):
        print(letras[columnas],'',end='')
    del columnas
    print()
    i = 1 # "i" es el numero que se imprime antes de cada fila horizontal
    for filas in tablero:
        print(f'{i:2d}', end='') # imprimimos el número i de cada fila con un par de espacios esteticos
        for columnas in filas:
            if columnas['testeado']:
                if columnas['enemigo']:
                    print(' x',end='') # si el jugador ya interactuó con la casilla y había un enemigo, imprimimos una "o"
                else: print(' o',end='') # si el jugador ya interactuó con la casilla y no había un enemigo, imprimimos una "x"
            else: print(vac,end='') # "vac" es la variable con el caracter que representa espacios vacios
        print()
        i += 1 # contador
    print("") # información para el usuario:
    print(f"Enemigos: {enemigos}")
    print(f"Disparos: {disparos}")

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
                    print(' x',end='')
                else: print(' o',end='')
            else:
                if columnas['enemigo']:
                    print(oc,end='') # si el jugador no interactuo todavia pero hay un enemigo, se lo revelamos con el caracter "oc" de ocupado
                else: print(vac,end='') # de lo contrario imprimimos el caracter de vacio
        print()
        i += 1
    print("")
    print(f"Enemigos: {enemigos}")
    print(f"Disparos: {disparos}")

# FUNCIÓN QUE GENERA ENEMIGOS
def gen_enemigos(cantidad_deseada,tablero):
    while cantidad_deseada > 0: # vamos yendo a casillas aleatorias y agregando enemigos si no los había antes, al agregar uno
                                # nuevo descontamos 1 de la cantidad de enemigos hasta llegar a 0 cuando esten todos los enemigos puestos
        fila = random.randint(0,len(tablero)-1)
        columna = random.randint(0,len(tablero)-1)
        if not tablero[fila][columna]['enemigo']:
            tablero[fila][columna]['enemigo'] = True
            tablero[fila][columna]['vivo'] = True # por defecto los enemigos estan vivos
            cantidad_deseada -= 1

# FUNCIÓN QUE ESTABLECE LA CANTIDAD DE DISPAROS SEGÚN LA DIFICULTAD
def get_disparos(dimensiones,dificultad):
  dimtotal=dimensiones**2 # las casillas son el cuadrado de los lados
  if dificultad == 1: # dificultad facil, disparos = 70% del total de casillas
    facil=dimtotal*0.7
    facilint=int(facil)
    if facil-facilint > 0.1:
      facil=(facil-(facil-facilint))+1 # redondeos
    else:
      facil=int(facil-(facil-facilint))
    return facil
  elif dificultad == 2: # dificultad media, disparos = 50% del total de casillas
    intermedio=dimtotal*0.5
    intermedioint=int(intermedio)
    if intermedio-intermedioint > 0.1: 
      intermedio=(intermedio-(intermedio-intermedioint))+1 # redondeos
    else:
      intermedio=intermedio-(intermedio-intermedioint)
    return intermedio

  elif dificultad == 3: # dificultad dificil, disparos = 30% del total de casillas
    dificil=dimtotal*0.3 
    dificilint=int(dificil)
    if dificil-dificilint > 0.1:
      dificil=(dificil-(dificil-dificilint))+1 # redondeos 
    else:
      dificil=dificil-(dificil-dificilint)
    return dificil

# FUNCIÓN PARA "DESCIFRAR" COORDENADAS
def getCoordenada(coord:str):
  coord = ''.join(sorted(list(coord))) # hacemos un sort para que, por ejemplo, A2 sea lo mismo que 2A
  coordsVert = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9} # equivalencias de las letras en numeros
  if len(coord) == 2: # nos aseguramos que el usuario haya introducido dos caracteres, que serian la letra y el numero de la casilla
    fila = int(coord[0])-1 # las filas son el numero que corresponde al indice 0 de la coordenada
    columna = coordsVert[(coord[1]).lower()] # las columnas son el numero que corresponde a la letra de indice 1 que introdujo el usuario, segun el diccionario coordsVert
  else:
    if (int(coord[0]) == 0) and (int(coord[1]) == 1) and (type(coord[2]) == str): # si hay mas de 2 caracteres, y tiene el estilo "01X", es la fila 10, columna X
      fila = 9
      columna = coordsVert[(coord[2]).lower()]
  return fila,columna

# FUNCIÓN PARA DISPARAR
def disparar(tablero,disparos,fila,columna):
    if disparos > 0:
        try: # un try para evitar errores si el usuario introduce algo mal 
          if tablero[fila][columna]['testeado']:
              print('Ya intentaste en esta casilla, prueba otra')
          else:
              if tablero[fila][columna]['enemigo']:
                  golpe = True # si hay un enemigo, golpeamos
              else:
                  golpe = False
          hit = True # "hit" es una variable que determina si la casilla es valida, en este caso si, entonces luego descontaremos un disparo
        except:
          hit = False # si hay un error "hit" es falsa, no descontaremos disparos del usuarios
    else:
      print('No tienes disparos disponibles')
      hit = False # "hit" es falsa también si no hay disparos disponibles
    return golpe, hit

# FUNCIÓN DE PRUEBAS SIMULADAS
def probar(dim:int,enem:list,shots:list):
  testablero = gen_tablero(dim)
  disparos = len(shots)
  enemigos = len(enem)
  for coord in enem:
    # Generación de los enemigos establecidos
    fila,columna = getCoordenada(coord)
    testablero[fila][columna]['enemigo'] = True
    testablero[fila][columna]['testeado'] = False
    testablero[fila][columna]['vivo'] = True
  for coord in shots:
    # Disparos establecidos
      fila,columna = getCoordenada(coord)
      golpe,hit = disparar(testablero,disparos,fila,columna)
      if golpe == True:
        testablero[fila][columna]['testeado'] = True
        testablero[fila][columna]['vivo'] = False
        enemigos -= 1
      else:
        testablero[fila][columna]['testeado'] = True
      if hit == True:
        disparos -= 1
  eye_spy(testablero)
  if enemigos == 0:
    print(f'GANASTE! te sobraron {disparos} disparos!')
    input('Pulsa ENTER para continuar...')
  else:
    print('PERDISTE!')
    input('Pulsa ENTER para continuar...')
  pass



############################
##### MENU Y EJECUCION #####
############################
x = None
while x != 5:
    limpiar()
    x = intinput('''
╔════════════════════╗
║ ¿Que deseas hacer? ║
╚════════════════════╝

╔════════════════════╗
║  1) Jugar          ║
║  2) Instrucciones  ║
║  3) Reglas         ║
║  4) Test           ║
║  5) Salir          ║
╠════════════════════╝
║
╚> Opcion (1/2/3/4/5): ''')
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
        
        # llamar a todas las funciones
        tablero = gen_tablero(dim)
        gen_enemigos(cantidad_deseada,tablero)
        disparos = int(get_disparos(dim,dif))
        enemigos = cantidad_deseada
        while (enemigos > 0) and (disparos > 0) and (enemigos <= disparos): # el juego continua mientras haya disparos y enemigos y haya oportunidad de ganar
          limpiar()
          if xray == True: eye_spy(tablero) # si xray es verdadero, mostramos donde estan los enemigos
          else: mostrar_tablero(tablero,enemigos) 
          print("")
          coord = input('Introduce la coordenada a disparar, o escribe "salir" para salir:\n> ')
          if coord.lower() == 'salir': break
          try:
            fila,columna = getCoordenada(coord) # convertir lo que introduce el usuario a una coordenada valida
            golpe,hit = disparar(tablero,disparos,fila,columna)
            if golpe == True: # dependiendo de si el golpe fue verdadero cambiamos las propiedades del diccionario de esa coordenada
              tablero[fila][columna]['testeado'] = True
              tablero[fila][columna]['vivo'] = False
              enemigos -= 1
              print('GOLPE!')
              input('Pulsa ENTER para continuar...')
            else:
              tablero[fila][columna]['testeado'] = True
              print('Fallaste!')
              input('Pulsa ENTER para continuar...')
            if hit == True: # si el disparo fue valido descontamos un disparo
              disparos -= 1
          except:
            print('Vuelve a intentarlo')
            input('Pulsa ENTER para continuar...')
        limpiar()
        mostrar_tablero(tablero,enemigos)
        xray = False
        
        if enemigos == 0:
          print(f'GANASTE! te sobraron {disparos} disparos!') # si todos los enemigos fueron derrotados el jugador gana
          input('Pulsa ENTER para continuar...')
        else:
          print('PERDISTE!')
          input('Pulsa ENTER para continuar...')
    elif x == 2:
      limpiar()
      print(r"""  
╔═════════════════╗
║  Instrucciones  ║
╚═════════════════╝
╔════════════════════════════════════════════════════════════════════════════════════════╗
║  - Para poder comenzar a jugar, selecciona la primera opcion (Jugar) del menú inicial. ║
║  - Elige el tamaño deseado del tablero.                                                ║
║  - Elige la cantidad de enemígos deseada.                                              ║
║  ┬ Selecciona el nivel de dificultad que deseas (Facil/Intermedio/Dificil),            ║
║  | esto determina la cantidad de disparos:                                             ║
║  └ Facil=70% del tablero / Intermedio=50% del tablero / Difícil=30% del tablero.       ║
║  - Se generara un tablero con letras en horizontal y numeros en vertical.              ║
║  - En dicho tablero habran enemigos escondidos en sus casillas.                        ║
║  - El objetivo es atacar las coordenadas del tablero en busca de los enemigos.         ║
║  ┬ ¡Ten cuidado! No puedes quedarte sin disparos disponibles o perderas.               ║
║  └ A su vez, si tu numero de disparos es menor a la cantidad de enemigos, perderas.    ║
║  - Una vez eliminados todos los enemigos, ganaras la batalla naval. ¡Suerte!           ║
╚════════════════════════════════════════════════════════════════════════════════════════╝ 
            """)
      input('Pulsa ENTER para continuar...')

    elif x == 3:
      limpiar()
      print(r"""
╔══════════╗
║  Reglas  ║
╚══════════╝
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  - El tablero no puede ser menor a 3x3 ni mayor a 10x10.                          ║
║  ┬ La cantidad de enemigos no puede superar el largo de los lados del tablero.    ║
║  └ Ej.: un tablero 5x5 no puede tener mas de 5 enemigos.                          ║
║  - No puedes disparar a una coordenada que esté fuera del tablero.                ║
╚═══════════════════════════════════════════════════════════════════════════════════╝ 
            """)
      input('Pulsa ENTER para continuar...')

    elif x == 4: # Ejecutar la funcion de prueba
      print('''Atencion, este modo es solo para realizar pruebas, por lo tanto, pueden haber errores, especialmente si 
no se siguen las instrucciones del juego. Por ejemplo, no introduzcas casillas fuera del rango del tablero.''')
      dim = intinput('Dimensiones del tablero: ')
      y = None
      enem = list()
      print('Introduce las coordenadas de los enemigos (deja en blanco para terminar):')
      y = input('Enemigo: ')
      while y != (''):
        enem.append(y) # agregar los enemigos que diga el usuario a la lista "enem"
        y = input('Enemigo: ')
      y = None
      shots = list()
      print('Introduce las coordenadas de los disparos (deja en blanco para terminar):')
      y = input('Disparo: ')
      while y != (''):
        shots.append(y) # agregar los disparos que diga el usuario a la listas "shots"
        y = input('Disparo: ')
      probar(dim,enem,shots) # ejecutar la prueba con la lista de enemigos y disparos
    elif x == 5:
      print('Saliendo...')
    elif x == 6: # OPCION 6 SECRETA, mensaje de error falso al que si se responde la frase "sv_cheats1 xray" se activa el modo para ver los enemigos
      if input('Error, pulsa ENTER para continuar... ') == 'sv_cheats1 xray':
        xray = True
        input('debug: xray activado')
    else:
      print('Esa no es una opcion')
      input('Pulsa ENTER para continuar...')