## Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
## A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = list()
def flota(mesg):
    while True:
        try: return float(input(mesg))
        except: print('Vuelve a intentarlo')
promedio = 0
mayor = 0
menor = 10
for i in range(5):
    x = flota('> ')
    while x < 0 or x > 10:
        print('La nota tiene que ser entre 0 y 10')
        x = flota('> ')
    notas.append(str(x))
    promedio += x
    if x > mayor:
        mayor = x
    if x < menor:
        menor = x
promedio /= 5
print(f'''
Las notas son: {', '.join(notas)}
El promedio es: {promedio}
La mayor fue: {mayor}
La menor fue: {menor}
''')