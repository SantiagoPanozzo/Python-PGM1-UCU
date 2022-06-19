# Escribir una función que recibe el Nombre de una canción y retorna el/los artista que la interpretan (utilizando diccionarios). Por ejemplo:

#get_artistas(‘All my loving’) -> ‘The Beatles’
#get_artistas(‘All along the watchtower’) -> [‘Bob Dylan’, ‘Jimi Hendrix']

def get_artistas(tema):
    database = {
        'all my loving':            'The Beatles',
        'all along the watchtower': ['Bob Dylan','Jimi Hendrix'], 
        'the power of love':        'Huey Lewis and The News',
        'never gonna give you up':  'Rick Astley',
        'lunita de tucuman':        'Tan Biónica',
        'cielo de un solo color':   'No Te Va Gustar',
        'the way':                  'Fastball',
    }
    if tema in database: return database[tema]
    else: print('La canción no se encuentra en la base de datos')

print(get_artistas(input('> '.lower())))