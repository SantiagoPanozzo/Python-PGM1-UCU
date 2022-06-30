def capicuar(palabra:str):
    comp1 = list()
    comp2 = list()
    a = 'aeiouAEIOU'
    b = 'áéíóúÁÉÍÓÚ'
    for x in palabra:
        if x in b: x = a[b.index(x)]
        comp1.append(x)
    comp2 = reversed(comp1)
    if ''.join(comp1).lower() == ''.join(comp2).lower(): return True
    else: return False

print(capicuar('Neuquén'))
print(capicuar('neuquén'))
print(capicuar('Neuquen'))
print(capicuar('neuquen'))
print(capicuar('reconocer'))
print(capicuar('Reconocer'))
print(capicuar('foo'))