año, mes, dia, edad = 0,0,0,0
año_actual = int(input('Año actual: '))
mes_actual = int(input('Mes actual (0-12): '))
# Forzar a que el mes tenga que ser entre entero y diciembre
while mes_actual < 1 or mes_actual > 12:
    print('Fuera de rango, vuelve a intentarlo')
    mes_actual = int(input('Mes actual (1-12): '))
# Si es un mes de 31 dias
if mes_actual == 1 or mes_actual == 3 or mes_actual == 5 or mes_actual == 7 or mes_actual == 8 or mes_actual == 10 or mes_actual == 12:
    dia_actual = int(input('Día (1-31): '))
    while dia_actual < 1 or dia_actual > 31:
        print('Fuera del rango, vuelve a intentarlo')
        dia_actual = int(input('Día actual (1-31): '))
# Si es febrero
elif mes_actual == 2:
    # Si es febrero en año bisiesto
    if año_actual%4 == 0:
        dia_actual = int(input('Día actual (1-29): '))
        while dia_actual < 1 or dia_actual > 29:
            print('Fuera del rango, vuelve a intentarlo')
            dia_actual = int(input('Día actual (1-29): '))
    # Si es febrero y no es año bisiesto
    else:
        dia_actual = int(input('Día actual (1-28): '))
        while dia_actual < 1 or dia_actual > 28:
            print('Fuera del rango, vuelve a intentarlo')
            dia_actual = int(input('Día actual (1-28): '))
# Si es un mes de 30 dias
elif mes_actual == 4 or mes_actual == 6 or mes_actual == 9 or mes_actual == 11:
    dia_actual = int(input('Día actual (1-30): '))
    while dia_actual < 1 or dia_actual > 30:
        print('Fuera del rango, vuelve a intentarlo')
        dia_actual = int(input('Día actual (1-30): '))

# Vuelvo a hacer lo mismo pero para la fecha de nacimiento
año = int(input('Año de nacimiento: '))
mes = int(input('Mes de nacimiento (0-12): '))
# Forzar a que el mes tenga que ser entre entero y diciembre
while mes < 1 or mes > 12:
    print('Fuera de rango, vuelve a intentarlo')
    mes = int(input('Mes de nacimiento (1-12): '))
# Si es un mes de 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dia = int(input('Día de nacimiento (1-31): '))
    while dia < 1 or dia > 31:
        print('Fuera del rango, vuelve a intentarlo')
        dia = int(input('Día de nacimiento (1-31): '))
# Si es febrero
elif mes == 2:
    # Si es febrero en año bisiesto
    if año_actual%4 == 0:
        dia = int(input('Día de nacimiento (1-29): '))
        while dia < 1 or dia > 29:
            print('Fuera del rango, vuelve a intentarlo')
            dia = int(input('Día de nacimiento (1-29): '))
    # Si es febrero y no es año bisiesto
    else:
        dia = int(input('Día de nacimiento (1-28): '))
        while dia < 1 or dia > 28:
            print('Fuera del rango, vuelve a intentarlo')
            dia = int(input('Día de nacimiento (1-28): '))
# Si es un mes de 30 dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dia = int(input('Día de nacimiento (1-30): '))
    while dia < 1 or dia > 30:
        print('Fuera del rango, vuelve a intentarlo')
        dia = int(input('Día de nacimiento (1-30): '))

# Calculo la edad primero con la diferencia de años
edad = año_actual - año - 1
# Si el mes actual es mayor al mes de nacimiento significa que ya cumplió años, entonces sumo un año
if mes < mes_actual:
    print(f'La edad de la persona es de {edad+1} años')
# Si es el mismo mes que su nacimiento, depende de si ya pasó el dia de su cumpleaños o no para sumarle el año
elif mes == mes_actual and dia < dia_actual:
    print(f'La edad de la persona es de {edad+1} años')
else:
    print(f'La edad de la persona es de {edad} años')