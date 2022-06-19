## Escribir una función que transforma una lista de listas con Nombres y apellidos, en una única lista con cada
## Nombre y apellido concatenados.
## Por Ejemplo:
##
## transformar_Nombres( [ [‘Rocky’, 'Balboa'] , [‘Muhammad’, 'Ali'] ] )
##
## devuelve [‘Rocky Balboa’, ‘Muhammad Ali’]

def transformar_Nombres(motherlist):
    x = list()
    for i in motherlist:
        x.append(' '.join(i))
    return x
print(transformar_Nombres([['Rocky', 'Balboa'] , ['Muhammad', 'Ali']]))