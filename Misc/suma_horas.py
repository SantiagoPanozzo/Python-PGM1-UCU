hora, minutos, segundos = 0, 0, 0
def leer(mesg, lim):
    global var
    while True:
        try: 
            var = int(input(f'Introduce {mesg} (0 a {lim}): '))
        except:
            print('Valor invalido, intentalo de nuevo')
        if var > lim:
            print('Valor mayor al límite, intentalo de nuevo')
        else:
            break
    return var

hora = leer('la hora',23)
minutos = leer('los minutos',59)
segundos = leer('los segundos',59)
hora2 = leer('la hora a sumar',int(87660/3))
minutos2 = leer('los minutos a sumar',int(5259600/3))
segundos2 = leer('los segundos a sumar',int(315576000/3))
hora_new = hora+hora2
min_new = minutos+minutos2
seg_new = segundos+segundos2
dias,años,bisiesto = 0,0,0
while seg_new >= 60:
    seg_new -= 60
    min_new += 1
while min_new >= 60:
    min_new -= 60
    hora_new += 1
while hora_new >= 24:
    hora_new -= 24
    dias += 1

while dias >= 365:
    if dias == 366 and años%4 == 0:
        dias -= 366
        años += 1
    else:
        dias -= 365
        años += 1

print(f'La hora {hora}h {minutos}m {segundos}s + {hora2}h {minutos2}m {segundos2}s es:')
print(f'{hora_new}h {min_new}m {seg_new}s')
if dias > 0:
    print(f'Se le suman {dias} días')
if años > 0:
    print(f'Se le suman {años} años')