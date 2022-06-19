def obtener_numero(mensaje,mini,maxi):
    def ingreso():
        while True:
            try:
                return(int(input(f'{mensaje} [{mini}:{maxi}]: ')))
            except: print('Número no valido, vuelva a intentarlo')
    x = ingreso()
    while x > maxi or x < mini:
        print('Número fuera del rango, vuelva a intentarlo')
        x = ingreso()
    return x

print(obtener_numero("¿Cúal es su número favorito?", -10,50))