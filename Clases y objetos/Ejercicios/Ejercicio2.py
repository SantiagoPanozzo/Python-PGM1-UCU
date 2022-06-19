# Implementar una clase Mascota que describa las mascotas. La clase debe tener las siguientes características:
# especie, Nombre, color y veterinaria. Implementar los métodos para acceder a los atributos y para imprimir el objeto.

class Mascota:
    def __init__(self,especie,Nombre,color,veterinaria):
        self.especie = especie
        self.Nombre = Nombre
        self.color = color    
        self.veterinaria = veterinaria
    def getEspecie(self):
        return self.especie
    def getColor(self):
        return self.color
    def getNombre(self):
        return self.Nombre
    def getVeterinaria(self):
        return self.veterinaria
    def __str__(self):
        return (f'Una mascota de especie {self.especie} llamada {self.Nombre} de color {self.color}, que va a la veterinaria {self.veterinaria}')

lapet = Mascota('labrador','Pipo','blanco','la cucha')
print(lapet)