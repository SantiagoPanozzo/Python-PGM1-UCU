'''Una cadena de caracteres se dice que tiene los caracteres de paréntesis balanceados, cuando todo
paréntesis que abre tiene su correspondiente paréntesis que cierra. En principio podemos pensar que
para que una cadena tenga los paréntesis balanceados, bastaría que la cantidad de paréntesis que abren
"(" sea igual a la cantidad de paréntesis que cierran, ")". Por ejemplo la siguiente cadena de caracteres
estaría balanceada:

"a = int(2 + 5/4 + (4 + 6))"    (son dos que abren y dos que cierran)

Sin embargo, siguiendo el mismo razonamiento el siguiente string también está balanceado:

"a = int(2 + 5))/4 + ((4 + 6)"   (tres abren y tres cierran, pero el segundo que cierra no tiene el
correspondiente que abre)

Realizar una función que reciba un string e indique si los paréntesis que tiene están balanceados.'''

def balparen(cadena):
    abiertos = 0
    cerrados = 0
    for i in cadena:
        if i == '(':
            abiertos+= 1
            if abiertos < cerrados:
                return False
        if i == ')':
            cerrados += 1
            if abiertos < cerrados:
                return False
    if abiertos == cerrados: return True
    else: return False

print(balparen('a = int(2 + 5/4 + (4 + 6))'))
print(balparen('a = int(2 + 5))/4 + ((4 + 6)'))