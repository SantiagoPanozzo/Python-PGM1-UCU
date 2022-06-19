# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dolar':'us$', 'Yen':'¥', 'Peso':'$', 'Real':'R$'},
# luego pregunte al usuario por una divisa y muestre su símbolo (o un mensaje de aviso si la divisa no está en el diccionario). 

constante1 = {'Euro':'€', 'Dolar':'us$', 'Yen':'¥', 'Peso':'$', 'Real':'R$'}
print(f'Divisas: {constante1.keys()}')
try: print(constante1[input('Divisa: ')])
except: print('La divisa no se encuentra en el diccionario')