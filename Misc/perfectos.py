for i in range(1,10001):
    suma = 1 
    for j in range(2,i):
        if i % j == 0:
            suma += j 
    if i == suma:
        print(i,'es perfecto')
