class punto:
    def __init__(self,pos_x,pos_y):
        self.__pos_x__ = pos_x
        self.__pos_y__ = pos_y
    def getX(self):
        return self.__pos_x__
    def getY(self):
        return self.__pos_y__
    def __str__(self) -> str:
        return f'X: {self.__pos_x__}, Y: {self.__pos_y__}'
class rectangulo:
    def __init__(self,vertice,alto:float,largo:float,color:str):
        self.__vertice__ = vertice
        self.__alto__ = alto
        self.__largo__ = largo
        self.__color__ = color
    def getVertice(self):
        return self.__vertice__
    def setVertice(self,vertice):
        self.__vertice__ = vertice
    def getAlto(self):
        return self.__alto__
    def setAlto(self,alto):
        self.__alto__ = alto
    def getLargo(self):
        return self.__largo__
    def setLargo(self,largo):
        self.__largo__ = largo
    def getColor(self):
        return self.__color__
    def setColor(self,color):
        self.__color__ = color
    def area(self):
        return round(self.__alto__*self.__largo__,2)
    def tamaño(self,x:float):
        self.setAlto(self.__alto__ * x)
        self.setLargo(self.__largo__ * x)
    def vertices(self):
        otro = punto(self.__vertice__.getX() + self.__largo__, self.__vertice__.getY() + self.__alto__) 
        return [self.__vertice__,otro]
    def clonar(self):
        return rectangulo(self.__vertice__,self.__alto__,self.__largo__,self.__color__)
    def __str__(self):
        return f'Rectangulo: \nVertice: {self.__vertice__}\nLargo: {self.__largo__}\nAlto: {self.__largo__}\nColor: {self.__color__}\nArea: {self.area()}'

primero = rectangulo(punto(10,10),30,20,'rojo')
segundo = primero.clonar()
segundo.setVertice(punto(segundo.getVertice().getX()+100,segundo.getVertice().getY()))
tercero = primero.clonar()
tercero.setVertice(punto(tercero.getVertice().getX(),tercero.getVertice().getY()+150))
tercero.tamaño(2)
print(primero,'\n')
print(segundo,'\n')
print(tercero,'\n')