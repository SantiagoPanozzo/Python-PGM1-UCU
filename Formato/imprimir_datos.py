# Básico de f-strings: Imprimir datos

# Imprime el cabezal
print()
print(f"{'i':>3}   {'i**2':>4}  {'i**3':>4} {'i**5':>6} {'i**10':>11}")
print(f"{'-'*3}   {'-'*4}  {'-'*4}  {'-'*6} {'-'*11}")

# Imprime los datos
for i in range(1,11):
    print(f"{i:3} {i**2:4} {i**3:5} {i**5:7} {i**10:11}")
print()