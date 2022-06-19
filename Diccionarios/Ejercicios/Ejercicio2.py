# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de una carrera
# {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación: 6, 'Redacción': 6, 'Trabajo final': 6}.
# Luego debe mostrar por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas de la carrera, y <créditos> son sus créditos. Al final debe mostrar
# también el número total de créditos.

perro = {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación': 6, 'Redacción': 6, 'Trabajo final': 6}
for i in perro:
    print(f'{i} tiene {perro[i]} créditos')
print(f'Número total de créditos: {sum(perro.values())}')