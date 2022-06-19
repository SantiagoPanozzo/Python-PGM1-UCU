codigo = input('Introduce el código del medidor: ')
lect_anterior = int(input('Introduce la lectura anterior (en número): '))
lect_actual = int(input('Introduce la lectura actual (en número): '))
while lect_actual < lect_anterior:
    print('La lectura actual no puede ser menor que la anterior, vuelve a intentarlo\n')
    lect_actual = int(input('Introduce la lectura actual: '))
consumido = lect_actual - lect_anterior 
gasto_fijo = 200
if consumido <= 500:
    costo = consumido * 2
elif consumido > 500 and consumido < 1000:
    costo = 500 * 1200
    consumido -= 500
    costo += consumido*5
elif consumido >= 1000:
    costo = 1000 * 4000
    consumido -= 1000
    costo += consumido * 9
costo += gasto_fijo
iva = costo*0.22
costo += iva
print(f'''

Código del medidor: {codigo}
Monto de la factura: {int(costo)}$

''')