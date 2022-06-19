# Ingresar números; devolver su suma y parar cuando se ingrese un cero
num = 1
resultado = 0
while num != 0:
    num = int(input('Ingresa un número: '))
    resultado += num
print('El resultado es',resultado)
