## Para utilizar un módulo es necesario importar el módulo mediante la declaración “import” seguido del Nombre del módulo.
## Utilizaremos el ya conocido módulo “random” y su función random.randint donde random.randint(1,6) devuelve un número aleatorio
## entre 1 y 6 (incluidos).
##
## b. Realizar un programa que cuente la cantidad de veces que salió la cara 1, 2, … 6 en 30 tiradas de dados. Esta vez resolver
## el ejercicio con la estructura de repetición for.
import random
resultados = list()
for i in range(30):
    resultados.append(random.randint(1,6))
print('En 30 tiradas de dados la cantidad de veces que salió cada cara fueron:')
for i in range(1,7):
    print(f'Cara {i}: {resultados.count(i)}')