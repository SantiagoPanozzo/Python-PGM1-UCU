### Dientessss
entrada = input('> ')
def dientes(entrada):
    ## pasamos la entrada a una lista
    intermedio = entrada.split(',')
    lista = list()
    ## pasamos los valores de esa lista a otra lista en forma de numeros enteros si son validos
    for i in intermedio:
        # ignoramos valores en blanco que puedan dar error
        if i == '': continue
        if len(str(i)) != 2:
            print('Uno de los valores ingresados no cumple el formato XX o no es un numero entero')
            return -1
        lista.append(int(i))
    ## esto es solo para ahorrarme escribir todos los números posibles
    posibles = []
    a = [11,19]
    for i in range(4):
        for i in range(a[0],a[1]):
            posibles.append(i)
        a[0] = a[0]+10
        a[1] = a[1]+10
    a = [51,56]
    for i in range(4):
        for i in range(a[0],a[1]):
            posibles.append(i)
        a[0] = a[0]+10
        a[1] = a[1]+10
    
    ## main
    #debug: print(posibles)
    #debug: print(lista)

    ## iteramos en la lista del usuario y la de posibles numeros, si un numero no es valido retornamos False, de lo contrario True
    for i in lista:
        #debug: print('next')
        valido = False
        for j in posibles:
            #debug: print('iteracion en posibles')
            if i == j:
                valido = True
                #debug: print('iteracion en posibles VERDADERA')
                break
        if valido == False:
            return False
    return True
            
print(dientes(entrada))