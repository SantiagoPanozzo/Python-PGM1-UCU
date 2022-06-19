# Programa para hacer conversiones del sistema binario al decimal y viceversa, así como operaciones simples con binarios
# Se aceptan números decimales no-enteros
# Cosas que hacer: arreglar la division

###################################
########### PRE-CODIGO ############
###################################

import os
## Funcion para la introducción de números enteros
def leer(mesg):
    while True:
        try:
            return(int(input(mesg)))
        except:
            print('Vuelve a intentarlo')


####################################
######### CÓDIGO PRINCIPAL #########
####################################

## Funcion inicial para elegir la herramienta
def inicio():
    os.system('cls')
    print('''
#################################################################
Programa para conversiones y operaciones con binarios y decimales
¿Qué deseas hacer?
1) Convertir
2) Operar
#################################################################
    ''')
    return(leer('Opción (0 para salir): '))

## Funcion del texto de convertir con opciones
def op_convert():
    os.system('cls')
    print('''
#########################################################
Programa para pasar de decimales a binarios y viceversa
¿Qué conversión deseas realizar?
1) Decimal a binario
2) Binario a decimal
#########################################################
    ''')
    return(leer('Opción (0 para salir): '))

## Funcion del texto de las operaciones con opciones
def op_operate():
    os.system('cls')
    print('''
#########################################################
Programa para realizar operaciones con números binarios
¿Qué operación deseas realizar?
1) Suma
2) Resta
3) Multiplicación
4) División
#########################################################
    ''')
    return(leer('Opción (0 para salir): '))

####################################
########### CONVERSIONES ###########
####################################

## Funcion para la conversión de decimal a binario
def dectobin(entrada):
    # Si hay una ',' o un '.', el número de entrada es decimal
    if ',' in entrada or '.' in entrada:
        # Hacemos una separacion entre la parte entera y la parte decimal (que sera 0.XYZ)
        decimales = ['0','.']
        enteros = list()
        # La variable 'separacion' solo dice si ya pasamos la coma o el punto, en principio es falso
        separacion = False
        for digitos in entrada:
            if digitos is ',' or digitos is '.':
                separacion = True
                # Si el digito en el que estamos es un coma o un punto, acabamos de atravesar la separacion
            elif (digitos is not ',' or digitos is not '.') and separacion is False:
                enteros.append(digitos)
                # Si el digito es un número y aún no atravesamos la separacion, estamos en un entero
            elif (digitos is not ',' or digitos is not '.') and separacion is True:
                decimales.append(digitos)
                # Si el digito es un número y ya atravesamos la separacion, estamos en un decimal
        entrada = int(''.join(enteros))
        decimales = float(''.join(decimales))
    else:
        decimales = 0
        entrada = int(entrada)
    # Calculamos los enteros
    resto = list()
    while entrada > 0:
        res = entrada//2
        resto.append(str(entrada%2))
        entrada = res
    resto.reverse()
    resto = ''.join(resto)
    # Calculamos los decimales
    salida_decimal = list()
    iteracion = 0
    if decimales != 0:
        salida_decimal.append(',')
        # Esta coma solo indica que empiezan los decimales
    while decimales != 0 and iteracion < 32:
        # el 32 es arbitrario, es solo para que no sea un loop infinito, same abajo antes del return
        decimales *= 2
        if decimales >= 1:
            salida_decimal.append('1')
            decimales -= 1
        else: salida_decimal.append('0')
        iteracion += 1
    salida_decimal = ''.join(salida_decimal)
    salida = resto+salida_decimal
    if iteracion >= 32:
        salida += '...'
    return salida

## Funcion para la conversión de binario a decimal
def bintodec(entrada):
    nums = list()
    a = 0
    longitud = len(entrada)-1
    for i in range(longitud,-1,-1):
        nums.append((int(entrada[i])*2**(a)))
        a += 1
    x = sum(nums)
    return(x)

###################################
########### OPERACIONES ###########
###################################

# Suma
def suma(a,b):
    x = bintodec(str(a))
    y = bintodec(str(b))
    z = x+y
    return(dectobin(z))
# Resta
def resta(a,b):
    x = bintodec(str(a))
    y = bintodec(str(b))
    z = x-y
    return(dectobin(z))
# Multiplicación
def multiplicacion(a,b):
    x = bintodec(str(a))
    y = bintodec(str(b))
    z = x*y
    return(dectobin(z))
# Division
def division(a,b):
    x = bintodec(str(a))
    y = bintodec(str(b))
    z = x//y
    return(dectobin(z))

#####################################
############# EJECUCIÓN #############
#####################################

while True:
    herramienta = inicio()
    if herramienta == 1:
        while True:
            conversion = op_convert()
            if conversion == 1:
                print(dectobin(input('Introduce un número de base 10: ')))
                input('Pulsa ENTER para continuar...')
            elif conversion == 2:
                print(bintodec(input('Introduce un número de base 2: ')))
                input('Pulsa ENTER para continuar...')
            elif conversion == 0:
                break
            else: pass
    elif herramienta == 2:
        while True:
            operacion = op_operate()
            if operacion == 1:
                print(suma((leer('A: ')),(leer('B: '))))
                input('Pulsa ENTER para continuar...')
            elif operacion == 2:
                print(resta((leer('A: ')),(leer('B: '))))
                input('Pulsa ENTER para continuar...')
            elif operacion == 3:
                print(multiplicacion((leer('A: ')),(leer('B: '))))
                input('Pulsa ENTER para continuar...')
            elif operacion == 4:
                print(division((leer('A: ')),(leer('B: '))))
                input('Pulsa ENTER para continuar...')
            elif operacion == 0:
                break
            else: pass
    elif herramienta == 0:
       break
    else: pass