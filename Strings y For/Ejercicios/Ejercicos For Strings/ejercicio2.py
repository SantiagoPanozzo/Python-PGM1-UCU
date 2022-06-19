## Realice lo mismo que en el ejercicio anterior, pero que escriba las letras del string en orden inverso
## (también una letra por línea). ¿Puede implementar las dos versiones propuestas?
string = input('> ')
if int(input('Version 1/2: ')) == 1:
    string2 = list()
    for i in string:
        string2.append(i)
    string2.reverse()
    for j in string2:
        print(j)
else:
    for i in range(len(string)-1,-1,-1):
        print(string[i])