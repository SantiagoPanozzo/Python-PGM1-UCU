# TA TE TI

# Debido a limitaciones de tiempo este codigo esta poco o nada optimizado, pero se ejecuta
# mis disculpas a quien tenga que leer este codigo
import os

class tateti():
    def __init__(self):
        self.__turno__ = 'x' # 
        self.__posiciones__ = dict()
    def JugarX(self,posicion):
        posicion = str(posicion)
        if self.__turno__ != 'x': print('No es su turno')
        else:
            #print('turno')
            tablero = self.getPos()
            ocupado = False
            try:
                if tablero[posicion] == ('x' or 'o'): ocupado = True
            except:
                pass
            if ocupado == False:
                tablero[posicion] = 'x'
                self.__turno__ = 'o'
            else: print('casillero ocupado')
    def JugarO(self,posicion):
        posicion = str(posicion)
        if self.__turno__ != 'o': print('No es su turno')
        else:
            ocupado = False
            #print('turno')
            tablero = self.getPos()
            try:
                if tablero[posicion] == ('x' or 'o'): ocupado = True
            except:
                pass
            if ocupado == False:
                tablero[posicion] = 'o'
                self.__turno__ = 'x'
            else: print('casillero ocupado')
    def getPos(self):
        return self.__posiciones__
    def reemplazo(self,a,tab,txt):
        try:
            txt = txt.replace(str(a),tab[str(a)])
        except: pass
        return txt
    def turn(self):
        return f'Turno de: {self.__turno__}'
    def __str__(self):
        tablero = self.getPos()
        texto = f"""
        [1][2][3]
        [4][5][6]
        [7][8][9]
        """
        try: texto = texto.replace('1',tablero['1'])
        except: pass
        try: texto = texto.replace('2',tablero['2'])
        except: pass
        try: texto = texto.replace('3',tablero['3'])
        except: pass
        try: texto = texto.replace('4',tablero['4'])
        except: pass
        try: texto = texto.replace('5',tablero['5'])
        except: pass
        try: texto = texto.replace('6',tablero['6'])
        except: pass
        try: texto = texto.replace('7',tablero['7'])
        except: pass
        try: texto = texto.replace('8',tablero['8'])
        except: pass
        try: texto = texto.replace('9',tablero['9'])
        except: pass
        return texto
    def Check(self):
        tablero = self.getPos()
        ganador = 'ninguno'
        if len(tablero) >= 9:
            if tablero['1'] == tablero['5'] == tablero['9']: ganador = tablero['1']
            if tablero['3'] == tablero['5'] == tablero['7']: ganador = tablero['3']
            if tablero['1'] == tablero['2'] == tablero['3']: ganador = tablero['1']
            if tablero['4'] == tablero['5'] == tablero['6']: ganador = tablero['4']
            if tablero['7'] == tablero['8'] == tablero['9']: ganador = tablero['7']
            if tablero['1'] == tablero['4'] == tablero['7']: ganador = tablero['1']
            if tablero['2'] == tablero['5'] == tablero['8']: ganador = tablero['2']
            if tablero['3'] == tablero['6'] == tablero['9']: ganador = tablero['3']
            return 'El juego ha finalizado'
        else:
            try:
                if tablero['1'] == tablero['5'] == tablero['9']: ganador = tablero['1']
            except: pass
            try:
                if tablero['3'] == tablero['5'] == tablero['7']: ganador = tablero['3']
            except: pass
            try:
                if tablero['1'] == tablero['2'] == tablero['3']: ganador = tablero['1']
            except: pass
            try:
                if tablero['4'] == tablero['5'] == tablero['6']: ganador = tablero['4']
            except: pass
            try:
                if tablero['7'] == tablero['8'] == tablero['9']: ganador = tablero['7']
            except: pass
            try:
                if tablero['1'] == tablero['4'] == tablero['7']: ganador = tablero['1']
            except: pass
            try:
                if tablero['2'] == tablero['5'] == tablero['8']: ganador = tablero['2']
            except: pass
            try:
                if tablero['3'] == tablero['6'] == tablero['9']: ganador = tablero['3']
            except: pass

        if (ganador == 'o') or (ganador == 'x'): return 'El juego ha finalizado'
        else: print('Tablero empatado')
        if ganador == 'ninguno':
            if len(tablero) < 9: # no todas las casillas ocupadas
                return 'El juego no ha terminado'
            
# funcion auxiliar para probar el juego
def intinput(mesg):
    while True:
        try: return int(input(mesg))
        except: print('Vuelve a intentarlo')
def limpiar():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

j = tateti()
while True:
    limpiar()
    print(j)
    print(j.turn())
    if j.Check() == 'El juego ha finalizado':
        print('El juego ha finalizado')
        break
    x = intinput('''
1- Jugar
2- Mostrar
3- Clean
4- Salir
> ''')
    if x == 1:
        y = intinput('''
1- x
2- o
> ''')
        z = intinput('Posicion: ')
        if y == 1:
            j.JugarX(z)
        elif y == 2:
            j.JugarO(z)
        input('Pulsa ENTER para continuar...')
    elif x == 2:
        print(j)
        print(j.Check())
        input('Pulsa ENTER para continuar...')
    elif x == 3:
        del j
        j = tateti()
    elif x == 4:
        exit()