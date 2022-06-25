## Escribir una función que abra 2 archivos indicados por parámetro y escriba un nuevo archivo con las líneas intercaladas
## de los archivos originales.

def intercalar(a1,a2):
    a1 = open(a1,'r')
    a2 = open(a2,'r')
    text1 = a1.readlines()
    text2 = a2.readlines()
    a3 = list()
    if len(text1) > len(text2):
        for c in range(len(text1)):
            if c == len(text2)-1: a3.append('\n')
            a3.append(text1[c])
            try: a3.append(text2[c])
            except: pass
    else:
        for c in range(len(text2)):
            try: a3.append(text1[c])
            except: pass
            if c == len(text1)-1: a3.append('\n')
            a3.append(text2[c])
    with open('output.txt','+w') as output:
        output.writelines(a3)
    print(''.join(a3))
    a1.close()
    a2.close()
intercalar(r'C:\Users\spa20\OneDrive\Sync\Python\Programacion 1\Python-PGM1-UCU\Archivos\Ejercicios\ja.txt',r'C:\Users\spa20\OneDrive\Sync\Python\Programacion 1\Python-PGM1-UCU\Archivos\Ejercicios\ja2.txt')