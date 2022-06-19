def traducir(es,eng,txt):
    txt = txt.split()
    traduccion = list()
    for i in txt:
        traduccion.append(eng[es.index(i)])
    return ' '.join(traduccion)

#print(traducir(input('> ').split(),input('> ').split(),input('> ')))

def translate():
    dicc = dict()
    x = input('ES: ')
    while x != '':
        dicc[x] = input('ENG: ')
        x = input('ES: ')
    text = input('Texto: ').split()
    traduccion = list()
    for words in text:
        traduccion.append(str(dicc.get(words, '--')))
    return ' '.join(traduccion)

print(translate())