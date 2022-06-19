import datetime
año, mes, dia, edad = 0,0,0,0
actual = datetime.datetime.now()
print(f'La fecha actual es {actual.day}/{actual.month}/{actual.year}')
# Funcion para leer datos numéricos
def leer(mesg):
    while True:
        try: 
            return(int(input(f'{mesg} ')))
        except:
            print('Vuelve a intentarlo')
año = leer('Año:')
if año == actual.year:
    print(' La persona tiene 0 años')
    exit()
while año > actual.year:
    print('El año introducido no puede ser mayor al actual')
    año = leer('Año: ')    
mes = leer('Mes (0-12):')
while mes > 12:
    print('Fuera de rango, vuelve a intentarlo')
    mes = leer('Mes (0-12):')
# Si es un mes de 31 días
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dia = leer('Día (1-31):')
    while dia < 1 or dia > 31:
        print('Fuera del rango, vuelve a intentarlo')
        dia = leer('Día (1-31):')
# Si es febrero
elif mes == 2:
    # Si es febrero en año bisiesto
    if año%4 == 0:
        dia = leer('Día (1-29): ')
        while dia < 1 or dia > 29:
            print('Fuera del rango, vuelve a intentarlo')
            dia = leer('Día (1-29):')
    # Si es febrero y no es año bisiesto
    else:
        dia = leer('Día (1-28):')
        while dia < 1 or dia > 28:
            print('Fuera del rango, vuelve a intentarlo')
            dia = leer('Día (1-28):')
# Si es un mes de 30 dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dia = leer('Día (1-30):')
    while dia < 1 or dia > 30:
        print('Fuera del rango, vuelve a intentarlo')
        dia = leer('Día (1-30):')
print(f'{dia}/{mes}/{año}')
edad = actual.year - año - 1
if mes < actual.month:
    print(f'La edad de la persona es de {edad+1} años')
elif mes == actual.month and dia < actual.day:
    print(f'La edad de la persona es de {edad+1} años')
else:
    print(f'La edad de la persona es de {edad} años')