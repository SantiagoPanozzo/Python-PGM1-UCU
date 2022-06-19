suma = 0
for i in range(1,int(input('N: '))):
    print(f'{i}/{2}^{i}')
    suma += i/(2**i)
print(suma)

print(sum([(i/(2**i)) for i in range(1,int(input('N: ')))]))