def leer(mesg):
    while True:
        try:
            var = int(input(mesg))
            return var
        except:
            print('Valor invalido, vuelve a intentarlo')
a = leer('Introduce el valor del primer lado: ')
b = leer('Introduce el valor del segundo lado: ')
c = leer('Introduce el valor del tercer lado: ')

if a**2 + b**2 == c**2:
    print('Es un triángulo rectángulo')
elif a**2 + c**2 == b**2:
    print('Es un triángulo rectángulo')
elif b**2 + c**2 == a**2:
    print('Es un triángulo rectángulo')
else: print('No es un triángulo rectángulo')