#  Implementar una clase Bicicleta que describa las bicicletas. La clase debe tener las siguientes características
# de una bici: marca, color, tamaño y si es de montaña o ciudad. Implementar los métodos para acceder a los atributos
# y para imprimir el objeto.

class bicicleta:
    # es una bici.
    def __init__(self,marca,color,tamaño,tipo):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo
    def getMarca(self):
        return self.marca
    def getColor(self):
        return self.color
    def getTamaño(self):
        return self.tamaño
    def getTipo(self):
        return self.tipo
    def __str__(self):
        return (f'Una bici de {self.tipo} marca {self.marca} de color {self.color}, rodado {self.tamaño}')

labici = bicicleta('GT','rojo','24','montaña')
print(labici)