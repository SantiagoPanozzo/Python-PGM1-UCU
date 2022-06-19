# Escribir una función que sanitiza una cadena. El método de sanitización es el siguiente:
#   a. Todas las letras con tilde se cambian por la misma letra sin tilde.
#   b. Símbolos de pregunta y de exclamación se reemplazan por guiones (“-“)
#   c. Los espacios se reemplazan por guiones bajos (“_")
#   d. La "ñ" se reemplaza por la “n"
#   e. Cualquier otro símbolo (que no sean letras) se remueve.

def sanitizar(cadena):
    cambios = {
        'á':'a','é':'e','í':'i','ó':'o','ú':'u','Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U',
        'ñ':'n','Ñ':'N','?':'-','!':'-','¿':'-','¡':'-',' ':'_'
        }
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = []
    for carac in cadena:
        if carac in letras:
            output.append(carac)
        elif carac in cambios:
            output.append(cambios[carac])
    return ''.join(output)

print(sanitizar('the quick brown fox jumped over the lazy dog While THEY aTe ñoquis mmm ¡¡¿sirve?!! --|+{}123'))