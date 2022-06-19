# Se usan paréntesis curvos o ninguno, no son modificables
tupla1 = (1,2,'a','b',1.5)
tupla1 = 1,2,'a','b',1.5
# tupla1[0] = 3 no funciona

# Para un solo elemento tenemos que agregar una coma al final
tupla2 = (1,)

# Accedemos a sus elementos de la misma manera que con las listas
tupla1[0] # >> 1

# También podemos medir su longitud de elementos
len(tupla1) # >> 5

# Para acceder al último (-1 en listas) hacemos esto:
tupla1[len(tupla1)-1] # >> 1.5

# Podemos tomar parte de ella
tupla1[1:3] # >> (2,'a')

# Tambien podemos concatenarlas
tupla3 = tupla1+tupla2
tupla3 # >> (1,2,'a','b',1.5,1)

# Podemos forzar reemplazar un elemento editando un copia de la tupla y reasignandola
tupla1 = (3,) + tupla1[1:] # >> 3,2,'a','b',1.5  #reemplazamos el primer elemento por 3

# Podemos usar una tupla para intercambiar variables sin tener que usar variables temporales
a = 2
b = 5
a,b = (b,a)
a # >> 5
b # >> 2
# si no usaramos una tupla se reemplazarian en orden y todaslas variables tendrian el mismo valor