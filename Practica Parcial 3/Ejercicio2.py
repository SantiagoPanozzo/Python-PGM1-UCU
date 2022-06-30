class personaje:
    def __init__(self,nombre:str):
        self.setNombre(nombre)
    
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
    
    def avanzar(self,lista_movimientos):
        for movimientos in lista_movimientos:
            if movimientos[0].lower() == ('norte'): self.setYe(self.getYe()+movimientos[1])
            if movimientos[0].lower() == ('sur'): self.setYe(self.getYe()-movimientos[1])
            if movimientos[0].lower() == ('oeste'): self.setEquis(self.getEquis()+movimientos[1])
            if movimientos[0].lower() == ('este'): self.setEquis(self.getEquis()-movimientos[1])
            self.__energia__ = self.getEnergia()-movimientos[1]