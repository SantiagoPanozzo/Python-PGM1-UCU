def caracteres_comunes(string1,string2):
    repetidas = []
    mays = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890'
    mins = 'abcdefghijklmnñopqrstuvwxyz1234567890' 
    for i in range(len(mays)):
        if (mays[i] in string1 or mins[i] in string1) and (mays[i] in string2 or mins[i] in string2):
            repetidas.append(mins[i])
    return repetidas

print(caracteres_comunes("banana", "Anana"))
print(caracteres_comunes("Programar", "picar código"))
print(caracteres_comunes("pepe", "juan"))