def leer(mesg):
    while True:
        try:
            var = int(input(mesg))
            return var
        except:
            print('Valor invalido, vuelve a intentarlo')

peso = leer('Introduce el peso (kg): ')
while peso < 0:
    print('El peso no puede ser negativo, vuelve a intentarlo')
    peso = leer('Introduce el peso (kg): ')

altura = leer('Introduce la altura (cm): ')
while altura < 0:
    print('La altura no puede ser negativa, vuelve a intentarlo')
    altura = leer('Introduce la altura (m): ')
altura /= 100
imc = peso / altura**2
print(f'El índice de masa corporal es de {imc}')
if imc < 18.5:
    print('La persona tiene bajo peso')
elif imc >= 18.5 and imc < 25:
    print('La persona tiene peso normal')
elif imc >= 25.0 and imc < 30:
    print('La persona tiene sobrepeso')
elif imc >= 30:
    print('La persona tiene obesidad')