def EnQuilibrio(cadena):
    def EsVocal(x):
        vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
        if x in vocales: return True
        else: return False
    vocales = 0
    list_vocales = list()
    for i in range(len(cadena)):
        if EsVocal(cadena[i]) == True:
            vocales += 1
            list_vocales.append(i)
    if vocales%2 == 0:
        return -1
    if len(list_vocales) == 1: return(list_vocales[0])
    else: return list_vocales[(len(list_vocales))//2]

print(EnQuilibrio('Programación'))
print(EnQuilibrio('perro'))
print(EnQuilibrio('pez'))
print(EnQuilibrio('Ágora'))