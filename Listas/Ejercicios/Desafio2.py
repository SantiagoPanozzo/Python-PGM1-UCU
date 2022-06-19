## Definir una función “traductor” que recibe por parámetro 2 listas con palabras, una lista con palabras en español y
## la otra con palabras en inglés. De acuerdo a la posición de la lista, se conoce la traducción de la misma, es decir
## en la posición x de la lista con palabras en inglés, está la traducción de la palabra en la posición x de la lista
## con palabras en español. La función recibe un tercer parámetro que es una frase y retorna una traducción sencilla de la frase.

## Ej.: traducir([“es”,“hoy”,“viernes”],[“is,“today”,“friday”],“Hoy es viernes”)  devuelve:  “today is friday”

def traducir(es,eng,txt):
    txt = txt.split()
    traduccion = list()
    for i in txt:
        traduccion.append(eng[es.index(i)])
    return ' '.join(traduccion)

print(traducir(input('> ').split(),input('> ').split(),input('> ')))