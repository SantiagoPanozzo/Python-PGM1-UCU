numero_entero = 25
numero_flotante = 2520.4598764

# Si el número tiene menos de 5 dígitos rellena con espacios a la izq. hasta llegar a 5 lugares
print(f'Número Entero: [{numero_entero:5d}]')

# Imprime el número con dos decimales, si la cnatidad de fígitos más uno (por el punto) es <, rellena a la
# izquierda con espacios hasta 10 lugares
print(f'Número Decimal: [{numero_flotante:10.2f}]')
# .Xf es X ceros despues del '.'
# el numero antes del punto son los espacios en blanco a colocar antes del número, Xf son X espacios en blanco antes del numero, menos la longitud del número
# si colocamos un 0 antes de la X, son X ceros que se agregan antes
# se pueden combinar como X.Yf, siendo X espacios en blanco y Y ceros despues del punto
# la 'd' es para decimales y la 'f' para floats

# Para rellenar con ceros a la izquierda se agrega el 0
print(f'Número Entero: [{numero_entero:05d}]')
print(f'Número Decimal: [{numero_flotante:010.2f}]')