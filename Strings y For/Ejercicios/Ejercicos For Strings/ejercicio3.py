## Escribir una función que reciba una cadena de caracteres y retorne una nueva cadena con los caracteres espacio (“ “)
## reemplazados por el carácter “;”
def semicolon(string):
    return string.replace(' ',';')
print(semicolon(input('> ')))