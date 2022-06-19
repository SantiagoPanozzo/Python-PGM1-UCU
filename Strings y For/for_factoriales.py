A = int(input('A: '))
B = int(input('B: '))
while B <= A:
    print('B tiene que ser mayor que A')
    B = int(input('B: '))
for i in range(A,B+1):
    valor = 1
    for j in range(1,i+1):
        valor *= j
    print(f'{i} {valor}')
