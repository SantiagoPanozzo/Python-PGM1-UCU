class personaje:
    def __init__(self,nombre:str):
        self.setNombre(nombre)
        self.__equis__ = 0
        self.__ye__ = 0
        self.__energia__ = 10
    def setNombre(self,nombre):
        self.__nombre__ = nombre
    def getNombre(self):
        return self.__nombre__
    def setEquis(self,equis:int):
        self.__equis__ = equis
    def getEquis(self):
        return self.__equis__
    def setYe(self,ye:int):
        self.__ye__ = ye
    def getYe(self):
        return self.__ye__
    def setEnergia(self,energia):
        self.__energia__ = energia
    def getEnergia(self):
        return self.__energia__
    
    def avanzar(self,lista_movimientos:list):
        for movimientos in lista_movimientos:
            if movimientos[1] <= self.getEnergia():
                if movimientos[0].lower() == ('norte'): self.setYe(self.getYe()+movimientos[1])
                if movimientos[0].lower() == ('sur'): self.setYe(self.getYe()-movimientos[1])
                if movimientos[0].lower() == ('este'): self.setEquis(self.getEquis()+movimientos[1])
                if movimientos[0].lower() == ('oeste'): self.setEquis(self.getEquis()-movimientos[1])
                self.__energia__ = self.getEnergia()-movimientos[1]
            else:
                print(f'No he podido completar el avance. Me he detenido en la posición {self.Ubicacion()}')
                break
    def CargarEnergia(self,unidades:int):
        self.setEnergia(self.getEnergia()+unidades)
    def Ubicacion(self):
        return (self.getEquis(),self.getYe())
    def Distancia(self,OtroPersonaje):
        here = self.Ubicacion()
        there = OtroPersonaje.Ubicacion()
        return (abs(here[0]-there[0]),abs(here[0]-there[0]))
    def __str__(self):
        return f'Nombre: {self.getNombre()}, Ubicacion: {self.Ubicacion()}, Energia: {self.getEnergia()}'

p1 = personaje('Bear')
p1.avanzar([('norte',2),('este',2)])
print(p1)
p2 = personaje('Carman')
p2.avanzar([('Sur',2),('Oeste',1),('Sur',4)])
p1.avanzar([('este',7),('norte',2)])
p1.CargarEnergia(10)
print(p1)
p1.avanzar([('este',7),('norte',2)])
print(p1.Distancia(p2))