def detectar_faltantes(stock,solicitud):
    cosas = dict()
    for piezas in solicitud:
        if piezas not in cosas: cosas[piezas] = 1
        else: cosas[piezas] += 1
    faltantes = dict()
    for i in cosas:
        if i not in stock:
            faltantes[i] = cosas[i]
        else:
            if cosas[i] > stock[i]: faltantes[i] = cosas[i] - stock[i]
    return faltantes

stock={"A":5, "B":7, "Z":2, "X":1}
solicitud=["A", "X", "A", "X", "B", "C"]
print(detectar_faltantes(stock,solicitud))
solicitud=["A", "X", "A", "X", "B", "C","D","Z"]
print(detectar_faltantes(stock,solicitud))
solicitud=["A", "X", "A", "X", "B", "C","D","A","A","A","Z"]
print(detectar_faltantes(stock,solicitud))
solicitud=["A", "X", "A", "X", "B", "C","D","A","A","A","A","Z"]
print(detectar_faltantes(stock,solicitud))

stockCustom = dict()
solicitudCustom = list()
p = ''
while p.lower() != 'salir':
    if p != '':
        if p not in stockCustom: stockCustom[p] = 1
        else: stockCustom[p] += 1
    p = input('Introduce un item para agregar al stock (escribe "salir" para terminar):\n> ')
    
p = ''
while p.lower() != 'salir':
    if p != '': solicitudCustom.append(p)
    p = input('Introduce un item para agregar a la solicitud (escribe "salir" para terminar):\n> ')

print(detectar_faltantes(stockCustom,solicitudCustom))