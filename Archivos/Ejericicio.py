class Alumno: 

    def __init__(self, nombre, apellido, curso, edad):
        self.setNombre(nombre)
        self.setApellido(apellido)
        self.setCurso(curso)
        self.setEdad(edad)

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getCurso(self):
        return self.__curso

    def setCurso(self, curso):
        self.__curso = curso

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f'Nombre: {self.__nombre}\nApellido: {self.__apellido}\nCurso: {self.__curso}\nEdad: {self.__edad}'

    def __repr__(self):
        return str(self)
Pepe = Alumno('Pepe','Gomez','Cuarto',10)
Juan = Alumno('Juan','Marquez','Quinto',11)
Felipe = Alumno('Mario','Mario','Sexto',10)
Lucas = Alumno('Lucas','Juarez','Primero',8)
Jorge = Alumno('Jorge','Joestar','Sexto',13)

alumnos = [Pepe,Juan,Felipe,Lucas,Jorge]
print(alumnos)

archivo = open('alumnos.txt','+w')
for pibes in alumnos:
    archivo.write(str(pibes) + '\n')
archivo.close()