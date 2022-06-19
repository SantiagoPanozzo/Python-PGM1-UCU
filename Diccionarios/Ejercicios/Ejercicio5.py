# Escribir una función que quita los elementos duplicados de una lista utilizando un diccionario. Debe retornar una nueva lista 
# sin elementos repetidos, sin importar el orden

def repedidont(lista):
    tupla = dict() # tampoco es una tupla
    for elementos in lista: tupla[elementos] = 'en este programa no se usan tuplas'
    return list(tupla)
print(repedidont(["string",222,2234.3,True,"string",222,2234.3,True,]))