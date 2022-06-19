# Escribir una función que permite organizar el envío masivo de emails para propagandas publicitarias. La función recibe un diccionario donde
# la clave es el Nombre de una persona y el valor asociado es una lista de sus Direcciones de correo electrónico (“emails”).
# Por ejemplo:

# emails={"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], "Marcela Rodríguez":["mleites@gmail.com", "rodriguez@gmail.com"],
# "Juan Lamas":["jlamasucu.edu.uy", "juan.lamas@gmail.com"]}

# La función debe devolver el diccionario, eliminando cualquier email que esté duplicado (dos personas pueden estar con el mismo email) y
# además debe eliminar cualquier email que no contenga al menos un carácter “@” y un carácter “.”

# Devolución con parámetro anterior:
# emails={"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], "Marcela Rodríguez":["mleites@gmail.com"],
# "Juan Lamas":["juan.lamas@gmail.com"]}

#Se eliminó "rodriguez@gmail.com" de Marcela porque ya existía y "jlamasucu.edu.uy" porque no tiene @. 

def maldad(lista):
    # estos diccionarios son intermedios para convertir datos:
    dict2 = dict()
    dict3 = dict()
    # personas son los Nombres, correo son las *LISTAS* de correos asignadas a cada Nombre (en caso de que alguien ponga un string funciona igual)
    for persona in lista:
        correo = lista[persona]
        if type(correo) is list:
            # iteramos por cada correo en la lista de correos de cada Nombre
            for i in correo:
                # si no tiene arroba o punto ya lo descartamos
                if ('@' or '.') not in i:
                    continue
                # si no esta ya en el dict2 lo agregamos, si esta repetido se descarta directamente
                if i not in dict2: dict2[i] = persona
                # funciona porque ahora son "correos:Nombres" en vez de "Nombres:correos", se entiende que
                # los Nombres no se van a repetir, pero si un correo se repite pasamos
        else: 
            # si el correo no fuera una lista no necesitamos iterar nada
            if correo not in dict2:
                if ('@' and '.') in i: dict2[correo] = persona
    # correo ahora pasa a ser los correos (keys) de dict2, persona pasa a ser los Nombres asignados a cada correo
    for correo in dict2:
        persona = dict2[correo]
        # pasamos los Nombres a keys del dict3 y los correos a su valor
        if persona not in dict3:
            dict3[persona] = [correo]
        else:
            # si ya hay un correo asignado a una persona, extendemos la lista para incluir el nuevo correo
            previos = list()
            previos.extend(dict3[persona])
            previos.extend([correo])
            dict3[persona] = previos
    return dict3

####################
### DEMOSTRACION ###
####################
emails = {
    "Martín Rodríguez":     ["arodri@ucu.edu.uy", "rodriguez@gmail.com"],
    "Marcela Rodríguez":    ["mleites@gmail.com", "rodriguez@gmail.com"],
    "John Smith":           "john@smith.com",
    "Juan Lamas":           ["jlamasucu.edu.uy", "juan.lamas@gmail.com","jlamasucu.edu.uy"],
    }

maldad(emails)