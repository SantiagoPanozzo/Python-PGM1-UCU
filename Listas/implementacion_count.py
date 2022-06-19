lista = ['e','l','e','f','a','n','t','e']
def contar(valor):
    global lista
    contador = 0
    for i in lista:
        if i == valor:
            contador += 1
    return contador
print(contar(input()))