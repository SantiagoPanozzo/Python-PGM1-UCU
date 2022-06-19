# Implementar una clase para identidades de personas. La clase debe tener los componentes usuales para la
# identificación de las personas como el número de la cédula, una dirección, Nombres y Apellidos, número de
# teléfono, etc. Se debe incluir métodos de acceso a todas las propiedades.

class persona:
    # es una persona.
    def __init__(self,Cedula,Direccion,Nombre,Apellido,Telefono):
        self.Cedula = Cedula
        self.Direccion = Direccion
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Telefono = Telefono 
    def getCedula(self):
        return self.Cedula
    def getDireccion(self):
        return self.Direccion
    def getNombre(self):
        return self.Nombre
    def getApellido(self):
        return self.Apellido
    def getTelefono(self):
        return self.Telefono 
    def Identificar(self):
        return {
            'nombre':       self.Nombre,
            'apellido':     self.Apellido,
            'direccion':    self.Direccion,
            'cedula':       self.Cedula,
            'telefono':     self.Telefono,
            }
juan = persona.Identificar(persona('3283343','Artigas 292','Juan','Fuentes','47323492'))
print(juan)