def promedio_de_kills(dias):
    kills = 0
    for i in dias:
        kills += i[1]
    return(kills/len(dias))
def promedio_movil(dias,n):
    promedios = list()
    enes = list()
    j = 0
    for i in range(len(dias)):
        enes.append(dias[i])
        j += 1
        if j == n:
            promedios.append(enes)
            enes = []
            j = 0
        elif (j != n) and (i+n-j >= len(dias)): # <--- ARREGLAR ESTO 
            promedios.append(enes)
            enes = []
            j = 0
    infectados = 0
    retorno = list()
    for i in promedios:
        cant_inf = 0
        infectados = 0
        for j in i:
            cant_inf += 1
            infectados += j[0]
        retorno.append(infectados/cant_inf)
    return retorno
lista=[ [3452, 45] , [2269, 53], [2318, 54], [1278, 33] , [2385, 41], [1185,31], [1234,13]]
print(promedio_de_kills(lista))
print(promedio_movil(lista,4))