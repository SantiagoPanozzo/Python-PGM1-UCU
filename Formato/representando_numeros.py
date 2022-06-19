# Básico de f-string: representando números

numero_flotante = 13.1416
numero_entero = 3871

print(f"Número Flotante: {numero_flotante:.2f}")
print(f"Número Flotante: {numero_flotante:8.4f}")
print(f"Número Flotante: {numero_flotante:08.4f}")
print(f"Número Flotante: {numero_flotante:e}")
print(f"Número Flotante: {numero_flotante:g}")
print(f"Número Entero: {numero_entero:6d}")
print(f"Número Entero: {numero_entero:06d}")
print(f"Número Entero en Hexa: {numero_entero:x}")
print(f"Número Entero en Binario: {numero_entero:b}")