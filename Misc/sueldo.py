# Programa para calcular el suelo neto mensual de un empleado, conociendo el pago por hora, número de horas trabajadas, impuestos y descuento (BPS y FONASA)
Nombre = input('Nombre del empleado: ')
while True:
    try:
        pago_hora = int(input('Pago por hora (pesos): '))
        break
    except:
        print('Introduce un número por favor')

while True:
    try:
        num_horas = int(input('Horas trabajadas: '))
        break
    except:
        print('Introduce un número por favor')

while True:
    try:
        bps = int(input('Descuento por BPS (%): '))
        break
    except:
        print('Introduce un número por favor')
bps = (bps / 100)

while True:
    try:
        fonasa = int(input('Descuento por FONASA (%): '))
        break
    except:
        print('Introduce un número por favor')

fonasa = (fonasa / 100)

pago_mes = pago_hora * num_horas
imp1 = pago_mes * bps
imp2 = pago_mes * fonasa
impuestos = imp1 + imp2
final = pago_mes - impuestos
print('El sueldo del empleado ',Nombre,' es de ',final,' pesos.')
