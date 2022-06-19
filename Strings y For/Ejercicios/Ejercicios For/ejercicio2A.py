## Para utilizar un módulo es necesario importar el módulo mediante la declaración “import” seguido del Nombre del módulo.
## Utilizaremos el ya conocido módulo “random” y su función random.randint donde random.randint(1,6) devuelve un número aleatorio
## entre 1 y 6 (incluidos).
## a. Realizar un programa para simular 20 tiradas de dos dados simultáneamente, dando el promedio de la suma de los resultados
## de los dos dados. Esta vez resolver el ejercicio con la estructura de repetición for.

import random
dado1 = 0
dado2 = 0
for i in range(20):
    dado1 += random.randint(1,6)
    dado2 += random.randint(1,6)
print(f'''
La suma de los resultados del primer dado es: {dado1}
La suma de los resultados del segundo dado es: {dado2}
El promedio es {(dado1+dado2)/2}
''')