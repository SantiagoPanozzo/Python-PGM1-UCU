'''import os
os.system('nvim') '''

oraciones = list()
while True:
    x = input()
    if x == '::q':
        break
    x = x.split('.')
    y = list()
    for i in x: # i es una lista
        if i == '':
            continue
        j = i.split() #j es una lista
        j[0] = j[0].title()
        j = ' '.join(j)
        jj = [j,'.']
        y.append(''.join(jj))
print(y)
print(len(y))
caracteres = 0
for i in y:
    caracteres += len(i)
print(caracteres)