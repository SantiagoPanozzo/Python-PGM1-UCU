# Una encuesta sobre la lectura de 3 revistas A, B y C, sea han obtenido los siguientes datos: de 10 personas,
# 6 leen la revista A, 5 la B, 5 la C, 2 la revistas B y C, 3 la C y A, 3 la A y B y 1 las tres.

# a) ¿Cuántos leen 2 y sólo 2 revistas? RESPUESTA: 5 
# b) ¿Cuántos no leen ninguna revista? RESPUESTA: 1
# c) ¿Cuántos leen 1 y sólo 1 revista? RESPUESTA: 3
# d) ¿Qué número de lectores tienen las 3 revistas? 1

a={"juan","pepe","maria","jose","esteban","lucia"}
b={"juan","pepe","marta","lucia","john"}
c={"lucia","john","maria","esteban","margarita"}

nombres = {
'AB': (a&b),
'BC': (b&c),
'CA': (c&a),
'DOS': ((a&b)|(b&c)|(c&a))-(a&b&c),
'ABC': (a&b&c),
'N': 10-len(a|b|c),
'soloa': (a-b-c),
'solob': (b-a-c),
'soloc': (c-a-b),
'UNA': (a-b-c)|(b-a-c)|(c-a-b),
}

print(f'''
a) ¿Cuántos leen 2 y sólo 2 revistas? RESPUESTA: {len(nombres['DOS'])} 
b) ¿Cuántos no leen ninguna revista? RESPUESTA: {nombres['N']}
c) ¿Cuántos leen 1 y sólo 1 revista? RESPUESTA: {len(nombres['UNA'])}
d) ¿Qué número de lectores tienen las 3 revistas? RESPUESTA: {len(nombres['ABC'])}
''')