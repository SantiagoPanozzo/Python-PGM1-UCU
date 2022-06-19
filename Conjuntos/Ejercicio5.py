def leer(mesg):
    while True:
        try: return(int(input(mesg)))
        except: print('Error: No es un número, vuelve a intentarlo')

conjunto = set()
print('Ingresa 5 números positivos, o uno negativo para terminar')
for i in range(5):
    x = (leer('Número: '))
    if x > 0:
        while str(x) in conjunto:
            print('El número ya fue ingresado, intenta uno diferente')
            x = leer('Número: ')
        conjunto.add(str(x))
    else: break
print(f'Números ingresados: {", ".join(conjunto)}')