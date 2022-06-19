#5. Escribir una clase que permita representar al personaje de un videojuego. Un personaje tiene un nombre (o nickname),
# un porcentaje de vida (o salud), un poder (su nombre, por ejemplo, “patada giratoria”), y una medida de daño (número entero
# entre 0 y 100).
#
#   1. Implementar un método que permite imprimir la información de un personaje utilizando la instrucción print()
#
#   2. Implementar un método que permite atacar a otro personaje (que se recibe cómo parámetro). El ataque del personaje (p1)
#   le quita vida al personaje que es atacado (p2), utilizando la siguiente función:
#
#        nueva_vida(p2) = vida_actual(p2) - medida_de_daño(p1)
#
#   3. Implementar un método que indica (devolviendo True) si un personaje está con vida (salud > 0)
#
#   4. Crear 3 personajes llamados pj1, pj2 y pj3 (con el porcentaje de salud y poder que ustedes desee), pj1 debe atacar  
#   a pj2 y pj3

class personaje:
    def __init__(self,Nombre,Salud,Poder,Danio):
        self.setNombre(Nombre)
        self.setSalud(Salud)
        self.setPoder(Poder)
        self.setDanio(Danio)
    def Informacion(self):
        print(f'''Nombre: {self.Nombre}
Salud: {self.Salud:1}
Poder: {self.Poder}
Danio: {self.Danio}''') 
    def getNombre(self):
        return self.Nombre
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    def getSalud(self):
        return self.Salud        
    def setSalud(self, Salud):
        self.Salud = Salud
    def getPoder(self):
        return self.Poder
    def setPoder(self, Poder):
        self.Poder = Poder
    def getDanio(self):
        return self.Danio
    def setDanio(self, Danio):
        if Danio > 100: Danio = 100
        if Danio < 0: Danio = 0 
        self.Danio = Danio
    def strike(self,char2):
        char2.setSalud((char2.getSalud())-(self.Danio))
    def convida(self):
        if self.Salud > 0:
            return True
        else: return False
    def __str__(self):
        return f'Nombre: {self.Nombre}\nSalud: {self.Salud}\nPoder: {self.Poder}\nDanio: {self.Danio}'

def combat(char1,char2):
    print(f'{char1.getNombre()} {char1.getPoder()} a {char2.getNombre()} por {char1.getDanio()} de HP!')
    pj1.strike(pj2)
    if char2.convida():
        print(f'{char2.getNombre()} {char2.getPoder()} a {char1.getNombre()} por {char2.getDanio()} de HP!')
        pj2.strike(pj1)
        if not char1.convida():
            print(f'{char1} ha muerto!')
    else: print(f'{char2} ha muerto!')

pj1 = personaje('pj1',50,'diezma',100)
pj2 = personaje('pj2',20,'ataca',10)
pj3 = personaje('pj2',10,'ataca',10)

combat(pj1,pj2)
combat(pj1,pj3)