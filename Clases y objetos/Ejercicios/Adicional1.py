class Auto:
	# un auto que arranca y se detiene
    def __init__(self, Marca, Color, Year,Capacidad,Rendimiento):
        self.setMarca(Marca)
        self.setColor(Color)
        self.setYear(Year)
        self.setCapacidad(Capacidad)
        self.setRendimiento(Rendimiento)
        self.arrancado = False
        self.Kilometraje = 0
        self.Combustible = 0
    def getMarca(self):
        return self.Marca
    def setMarca(self, Marca):
        self.Marca = Marca
    def getColor(self):
        return self.Color
    def setColor(self, Color):
        self.Color = Color
    def getYear(self):
        return self.Year
    def setYear(self, Year):
        self.Year = Year
    def getCapacidad(self):
        return self.Capacidad
    def setCapacidad(self,Capacidad):
        self.Capacidad = Capacidad
    def getRendimiento(self):
        return self.Rendimiento
    def setRendimiento(self,Rendimiento):
        self.Rendimiento = Rendimiento
    def getCombustible(self):
        return self.Combustible
    def setCombustible(self,Combustible):
        self.Combustible = Combustible
    def getKilometraje(self):
        return self.Kilometraje
    def setKilometraje(self,Kilometraje):
        self.Kilometraje = Kilometraje
    def arrancar(self):
        if self.arrancado == True:
            print('El auto ya esta en movimiento')
        else: 
            self.arrancado = True
            print('Arrancaste el auto')
    def detener(self):
        if self.arrancado == False:
            print('El auto ya esta detenido')
        else:
            self.arrancado = False
            print('Detuviste el auto')
    def cargar_nafta(self,litros):
        disponibles = self.Capacidad - self.Combustible
        if litros <= disponibles:
            self.Combustible += litros
            print(f'Cargados {litros} litros de nafta. Combustible actual: {self.Combustible}')
        else:
            self.Combustible += disponibles
            restantes = litros - disponibles
            print(f'Cargados {disponibles} litros hasta llenar el tanque. Sobraron {restantes} litros')
    def recorrer(self,kms):
        if self.arrancado == False: print('El auto no esta encendido.')
        else:
            recorrible = self.Rendimiento * self.Combustible
            if kms > recorrible: print(f'No hay combustible suficiente para recorrer {kms}km, alcanzaria solo para {recorrible}km')
            else:
                restante = (((recorrible-kms)/self.Rendimiento))
                self.setCombustible(restante)
                print(f'Recorridos los {kms}km, {self.Combustible} litros restantes')
    def __str__(self):
        return f'Un auto\nMarca: {self.Marca}\nColor: {self.Color}\nAño: {self.Year}\nCapacidad: {self.Capacidad} litros\nRendimiento: {self.Rendimiento} km/l'


elRayo = Auto('Mercedes','Rojo','1998',50,10)
print(elRayo)
elRayo.cargar_nafta(100)
elRayo.arrancar()
elRayo.recorrer(10)
elRayo.detener
print(elRayo.getCombustible())