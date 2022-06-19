# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por
# una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está
# en el diccionario debe mostrar un mensaje informando de ello. Repetir las preguntas hasta que el usuario ingrese la
# palabra fin (fin puede estar en mayúsculas o minúsculas).

#Fruta      Precio
#Banana     1.35
#Manzana    0.80
#Pera       0.85
#Naranja    0.70

def floatinput(mesg):
    while True:
        try: return float(input(mesg))
        except: 'Por favor ingrese un número'

precios = {
    'Banana':   1.35,
    'Manzana':  0.80,
    'Pera':     0.85,
    'Naranja':  0.70
}

keywd = ''
while keywd.lower() != 'fin':
    fruta = input('Fruta: ').title()
    while fruta not in precios:
        print('Esa fruta no está disponible, vuelve a intentarlo')
        fruta = input('Fruta: ').title()
    kilos = floatinput('Kilos: ')
    print(f'{kilos}kg de {fruta} tienen un precio de {kilos*precios[fruta]} pesos')
    keywd = input('Pulse ENTER para continuar, escriba "fin" para terminar...')