## Funciones para calcular y verificar el dígito verificador de un cédula
def digito_verificador(ci):
    # Como la entrada es un número entero la paso a cadena de texto
    ci = str(ci)
    # Paso todos los caracteres a una lista
    Cedula = list()
    for i in ci:
        Cedula.append(i)
    suma = 0
    valores = [2,9,8,7,6,3,4]
    # Iteramos los caracteres de la Cedula y los multiplicamos por el valor corresponiente de los multiplicadores
    if len(Cedula) == 7:
        for i in range(len(Cedula)):
            suma += int(Cedula[i]) * valores[i]
    # Si la Cedula es de 6 caracteres hacemos lo mismo pero ignorando el primero de los multiplicadores
    elif len(Cedula) == 6:
        for i in range(len(Cedula)):
            suma += int(Cedula[i]) * valores[i+1]
    # De lo contrario la Cedula no esta entre 100000 y 9999999, retornamos el -1
    else: return -1
    # Si la division entera es 0, retornamos 0, si es otro número hacemos el calculo de 10 menos el resto de la suma sobre 10
    division = suma//10
    if division == 0: return 0
    else:
        return 10-(suma%10)

# En esta otra funcion uso la anterior para calcular el verificador y comparo el resultado con el numero ingresado
def esValida(ci,dv):
    if dv == digito_verificador(str(ci)):
        return True
    else: return False

# DEMOSTRACION (se ingresan enteros siempre como dice la letra):
print(digito_verificador(int(input('Cedula a calcular: '))))
print(esValida(int(input('Cedula a comprobar: ')), int(input('Digito: '))))