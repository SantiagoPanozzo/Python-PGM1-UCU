def promedio_muertes(lista): return int((sum(list(i['muertos'] for i in lista))/len(lista)))

lista=[ { "casos": 3452, "muertos":45} , { "casos":2269, "muertos":53}, { "casos":2318, "muertos":54}, { "casos": 1278, "muertos":33} , { "casos": 2385, "muertos":41}, { "casos":1185, "muertos":31} ]
print(promedio_muertes(lista))

def movil(lista,n):
    promedios = list()
    test = list()
    for i in range(int(len(lista))):
        test.append('')
    for i in range(len(test)): test[i] = list()
    pos = 0
    for i in range(0,len(lista)+1):
        j = 0
        while j < n:
            try:
                test[pos].append(lista[i+j]['casos'])
            except:
                pass
            j += 1
        pos += 1
    for i in test:
        if i == []: continue
        promedios.append(sum(i)//len(i))
    return promedios
print(movil(lista,int(input('> '))))