veces = int(input('¿Cuantos numeros se van a sumar?: '))
total = 0
vez = 0
while vez < veces:
  num = int(input('Introducir numero: '))
  total = total + num
  vez = vez + 1
print(('El total es: {}').format(total))
