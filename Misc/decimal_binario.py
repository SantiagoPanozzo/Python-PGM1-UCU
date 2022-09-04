# Decimal a binario
import os
def leer(mesg):
    while True:
        try:
            return(int(input(mesg)))
        except:
            print('Vuelve a intentarlo')

def dectobin(entrada):
    entrada = int(entrada)
    resto = list()
    while entrada > 0:
        res = entrada//2
        resto.append(str(entrada%2))
        entrada = res
    resto.reverse()
    return resto
def bintodec(entrada):
    nums = list()
    a = 0
    longitud = len(entrada)-1
    for i in range(longitud,-1,-1):
        nums.append((int(entrada[i])*2**(a)))
        a += 1
    return(sum(nums))

def bin2dec(binary:str) -> int: return sum(list(reversed([int(x) for x in binary]))[z]*(2**z) for z in range(0,len(list(reversed([int(x) for x in binary])))))

def conversion():
    os.system('cls')
    print('''
#########################################################
Programa para pasar de decimales a binarios y viceversa
¿Qué conversión deseas realizar?
1) Decimal a binario
2) Binario a decimal
3) Salir
#########################################################
    ''')
    return(leer('Opción: '))
def convertir():
    opcion = conversion()
    while opcion != 3:
        if opcion == 1:
            n = input('Introduce un número de base 10: ')
            print(f"El número {n} en binario es: {''.join(dectobin(n))}")
            input('Pulsa ENTER para continuar...')
        elif opcion == 2:
            n = input('Introduce un número de base 2: ')
            print(f"El número {n} en decimal es: {(bin2dec(n))}")
            input('Pulsa ENTER para continuar...')
        elif opcion == 3:
            inicio()
        else:
            print('Vuelve a intentarlo')
        # Volver a pedir la opcion de continuar:
        opcion = conversion()

def suma(a,b):
    x = bintodec(a)
    y = bintodec(b)
    z = y+x
    return(''.join(dectobin(z)))
def resta(a,b):
    x = bintodec(a)
    y = bintodec(b)
    z = y-x
    return(''.join(dectobin(z)))
def division(a,b):
    x = bintodec(a)
    y = bintodec(b)
    z = y%x
    return(''.join(dectobin(z)))
def multiplicacion(a,b):
    x = bintodec(a)
    y = bintodec(b)
    z = y*x
    return(''.join(dectobin(z)))
def operaciones():
    seguir = True
    while seguir == True:
        eleccion = leer('''
################################################################
Programa para realizar operaciones con números binarios
¿Qué operación deseas realizar?
1) Suma
2) Resta
3) Multiplicación
4) División
5) Salir
################################################################

Opcion: ''')
        if eleccion == 1:
            a = leer('A: ')
            b = leer('B: ')
            print(suma(a,b))
        elif eleccion == 2:
            a = leer('A: ')
            b = leer('B: ')
            print(resta(a,b))
        elif eleccion == 3:
            a = leer('A: ')
            b = leer('B: ')
            print(multiplicacion(a,b))
        elif eleccion == 4:
            a = leer('A: ')
            b = leer('B: ')
            print(division(a,b))
        elif eleccion == 5:
            inicio()
        else:
            print('Vuelve a intentarlo')

def inicio():
    iniciacion = leer('''
#################################################################
Programa para conversiones y operaciones con binarios y decimales
¿Qué deseas hacer?
1) Convertir
2) Operar
3) Salir
################################################################

Opcion: ''')
    if iniciacion == 1:
        convertir()
        return(True)
    elif iniciacion == 2:
        operaciones()
        return(True)
    elif iniciacion == 3:
        return(False)
    else:
        print('Vuelve a intentarlo')
        return(True)

seguir = True
while inicio() == True:
    inicio()