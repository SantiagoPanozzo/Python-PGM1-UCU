color = input("Ingrese el color de la bicicleta: ")
marca = input("Ingrese la marca de la bicicleta: ")
tamaño = input("Ingrese el tamaño de la bicicleta: ")
tipo = input("La bicicleta es de montaña o ciudad?: ")
class Bici:
    #Contiene las características de una bici.
    def __init__ (self, marca, color, tamaño, tipo):
        self.color= color
        self.marca= marca
        self.tamaño= tamaño
        self.tipo= tipo
    def getMarca(self):
        return self.marca
    def getColor(self):
        return self.color
    def getTamaño(self):
        return self.tamaño
    def getTipo(self):
        return self.tipo
    def __str__(self):
        return "a"
        #return ("Es una bicicleta de color "+self.color+", cuya marca es "+self.marca+", de tamaño"+self.tamaño+", y está hecha para la "+self.tipo)
bicicleta = Bici(marca, color, tamaño, tipo)
print(Bici)