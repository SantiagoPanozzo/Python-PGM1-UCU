A = {i**2 for i in range(1,1000)}
B = {i**3 for i in range(1,1000)}
C = {576, 676, 784, 529, 625, 729, 7744, 7569}

if A&C == C: conjuntito = 'Si'
else: conjuntito = 'No'

print(f'''
¿Qué elementos están presentes en ambos conjuntos? ¿cuántos son?
    - {', '.join(str(i) for i in (A&B))}

¿El conjunto .(576, 676, 784, 529, 625, 729, 7744, 7569). son números obtenidos por elevar un natural al cuadrado?
    - {conjuntito}''')