## Rúbrica: Escribir una función que tenga como parámetro una lista con precios y devuelva el menor
## y el mayor de los precios.
lista = list()
p = 0
print('Introduce los precios (formato número ej.:123)')
print('Escribe "x" en cualquier momento para terminar')
while True:
    x = input(f'Precio {p+1}: ')
    if x == 'x' or x == 'X': break
    else:
        lista.append(float(x))
        p += 1
mayor = (lista[0])-1
menor = (lista[0])-1
for i in lista:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i
print(f'El precio mayor es {mayor} y el menor es {menor}')