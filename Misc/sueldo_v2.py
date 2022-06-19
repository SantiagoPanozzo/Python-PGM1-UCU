# Programa para calcular el suelo neto mensual de un empleado, conociendo el pago por hora, número de horas trabajadas, impuestos y descuento (BPS y FONASA) 
Nombre = input('Nombre del empleado: ')
# Defino una funcion para leer las variables, con 'varia' como el Nombre 
# de la variable, y 'mesg' como el mensaje que se muestra al usuario
def introduccion(mesg):
    while True:
        try:
            global varia
            varia = int(input(mesg))
            break
        except:
            print('Eso no es un número, vuelve a intentarlo')
introduccion('Pago por hora: ')
pago_hora = varia
introduccion('Horas trabajadas: ')
num_horas = varia
introduccion('Descuento por BPS (%): ')
bps = (varia/100)
introduccion('Descuento por FONASA (%): ')
fonasa = (varia/100)
pago_mes = pago_hora * num_horas
imp1 = pago_mes * bps
imp2 = pago_mes * fonasa
impuestos = imp1 + imp2
final = pago_mes - impuestos
print('El sueldo del empleado ',Nombre,' es de ',final,' pesos.')