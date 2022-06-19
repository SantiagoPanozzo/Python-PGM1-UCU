def long(entrada):
    print(entrada)
    contador = 0
    for i in entrada:
        contador += 1
    return contador
print(long((input('> ').split())))