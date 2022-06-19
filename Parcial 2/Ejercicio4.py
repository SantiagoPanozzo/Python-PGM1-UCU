'''Escribir una función que permita generar contraseñas en forma aleatoria. La función recibirá como
parámetros, la cantidad total de caracteres que debe tener la contraseña y cuántos de ellos deben ser
números. La función utilizará todas las letras del abecedario en minúscula y los números del 0 al 9. 

Ej.: genera_contraseña(8, 2) ---> “rgh7u4uj”'''

import random
from random import randint, shuffle, choice
def genera_contraseña(longitud, nums):
    letras = 'abcdefghijklmnñopqrstuvwxyz'
    numeros = '0123456789'
    passwd = []
    for i in range(longitud):
        passwd.append('-')
    while '-' in passwd:
        j = randint(0,len(passwd)-1)
        if passwd[j] == '-':
            if nums > 0:
                passwd[j] = numeros[randint(0,len(numeros)-1)]
                nums -= 1
            else:
                passwd[j] = letras[randint(0,len(letras)-1)]
    return ''.join(passwd)

def pass_gen(lengt,nums):
    lett = 'abcdefghijklmnñopqrstuvwxyz'
    numb = '0123456789'
    passwd = []
    for i in range(nums):
        passwd.append(str(choice(numb)))
    for i in range(lengt-nums):
        passwd.append(str(choice(lett)))
    shuffle(passwd)
    return ''.join(passwd)

# Demostración, 20 contraseñas
for i in range(20):
    print(pass_gen(8,2))