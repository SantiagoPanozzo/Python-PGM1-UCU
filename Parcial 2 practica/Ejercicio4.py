def palabras(parrafo):
    cantidad = 0
    while parrafo[-1] == ' ':
        parrafo = parrafo[:-1]
    while parrafo[0] == ' ':
        parrafo = parrafo[1:]
    for i in range(len(parrafo)):
        if parrafo[i] == ' ' and parrafo[i-1] != ' ':
            cantidad += 1
    return cantidad+1
print(palabras('Loren ipsum revitalis et preces me telt de'))
print(palabras('   Loren   ipsum  revitalis et  preces me  telt de        ')) # Funciona aunque hayan espacios innecesarios