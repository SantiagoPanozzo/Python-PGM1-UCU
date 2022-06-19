suma = 0
for i in range(2,(int(input('N: '))+1)):
    suma += (i*i)/((i-1)*(i+1))
print(suma)
