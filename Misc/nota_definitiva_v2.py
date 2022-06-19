# Programa para calcular el promedio de cuatro notas con la ponderación: 25%, 15%, 20%, 40%
# Definimos funcion con argumento 'num' (numero del parcial), y almacenamos lo leido en 'var'
def parcial(num):
    while True:
        global var
        try:
            var = int(input(('Porcentaje del {} parcial: ').format(num)))
            break
        except:
            print('Eso no es un número')
# Llamamos a la funcion y vamos asignando lo leido en 'var' a variables diferentes
parcial('primer')
parcial1 = var
parcial('segundo')
parcial2 = var
parcial('tercer')
parcial3 = var
parcial('cuarto')
parcial4 = var
parcial1 *= 0.25
parcial2 *= 0.15
parcial3 *= 0.20
parcial4 *= 0.40
final = parcial1 + parcial2 + parcial3 + parcial4
print('La nota final es de:',final,'%')