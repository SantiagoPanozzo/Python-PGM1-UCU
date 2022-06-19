# Funciones polinomiales
from math import sqrt
import math
def polipos(a,b,c):
    x = (-b+sqrt(b**2-4*a*c))/(2*a)
    return x
def polineg(a,b,c):
    x = (-b-sqrt(b**2-4*a*c))/(2*a)
    return x
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
print(f'X1: {polipos(a,b,c)}, X2: {polineg(a,b,c)}')