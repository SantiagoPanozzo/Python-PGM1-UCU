## Implementar la diferencia simétrica de dos listas. La diferencia simétrica consiste en todos los elementos de la primera
## lista que no están en la segunda y de todos los elementos de la segunda lista que no están en la primera.
## Por ejemplo difsim([1, 2, 3], [3, 4, 5]) devuelve [1, 2, 4, 5]. El resultado no debe tener duplicados.
def difsim(list1,list2):
    list3 = list()
    for i in list1:
        isin = False
        for j in list2:
            if i == j:
                isin = True
        if isin == False:
            list3.append(i)
    for i in list2:
        isin = False
        for j in list1:
            if i == j:
                isin = True
        if isin == False:
            list3.append(i)
    return list3

## DEMOSTRACION
def listar(lista, mesg):
    while True:
        x = input(mesg)
        if x != '':
            lista.append(x)
        else: break
lista1 = list()
listar(lista1,'1> ')
lista2 = list()
listar(lista2,'2> ')
print(difsim(lista1,lista2))