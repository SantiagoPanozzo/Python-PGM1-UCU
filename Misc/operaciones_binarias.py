def leer(mesg):
    while True:
        try:
            return(int(input(mesg)))
        except:
            print('Vuelve a intentarlo')

def introduccion(mesg):
    valid = False
    while valid is False:
        entrada = input(mesg)
        errors = 0
        for i in range (0,(len(entrada)+1)):
            if entrada[i] != '1' or entrada[i] != '0':
                errors += 1
        if errors == 0:
            valid = True
        else:
            valid = False
            print('Número no binario, vuelve a intentarlo')
    print(entrada)
introduccion('A: ')
                