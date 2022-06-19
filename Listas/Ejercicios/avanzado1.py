## Implementar una función que recibe una lista como parámetro y devuelve una nueva lista eliminando elementos duplicados
def nodupes(lista):
    x = list()
    for i in lista:
        if not lista.count(i) > 1:
            x.append(i)
    return x

## DEMOSTRACION:
def listar(lista, mesg):
    while True:
        x = input(mesg)
        if x != '':
            lista.append(x)
        else: break
ejlista = list()
listar(ejlista,'> ')
print(', '.join(nodupes(ejlista)))