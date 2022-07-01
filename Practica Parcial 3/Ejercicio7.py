##  Escribir una función que recibe como parámetros:
##      a) el nombre (ubicación y nombre con extensión) de un archivo
##      b) una cadena de caracteres
##  y retorna la cantidad total de veces que esa cadena aparece en el archivo

## Nota: la cadena puede estar formada por uno o varios caracteres. Por ejemplo,
## un espacio " , una letra "z", o por varios carateres "¡Hola!".

# ! modificarlo usando try:except para controlar que el usuario pase como parámetro un nombre de archivo válido

def cuentacadenas(ruta,cadena):
    try:
        with open(ruta,'r') as archivo:
            return (archivo.read()).count(cadena) 
    except: return -1
print(cuentacadenas(r'C:\Users\spa20\OneDrive\Sync\Python\Programacion 1\Python-PGM1-UCU\Archivos\Ejercicios\ja.txt','ola'))
print(cuentacadenas(r'C:\Users\spa20\OneDrive\Sync\Python\Programacion 1\Python-PGM1-UCU\Archivos\Ejercicios\j.txt','ola'))