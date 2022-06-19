# Programa que convierte la temperatura leída en celsius a fahrenheit
# celcius = (5/9)*(fahrenheit-32)

def ftoc(x):
    return((5/9)*(x-32))


print('La temperatura en celcius es',ftoc(int(input('Temperatura en fahrenheit: '))))

