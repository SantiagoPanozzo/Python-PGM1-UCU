class Jugador:
    def __init__(self,Nombre:str,Cedula:int,Numero:int,Posicion:str,Valoracion:int):
        self.setNombre(Nombre)
        self.setCedula(Cedula)
        self.setNumero(Numero)
        self.setPosicion(Posicion) 
        self.setValoracion(Valoracion)
    def getNombre(self):
        return self.Nombre
    def setNombre(self,Nombre):
        self.Nombre = Nombre.title()
    def getCedula(self):
        return self.Cedula
    def setCedula(self,Cedula):
        if len(str(Cedula)) == 8:
            self.Cedula = Cedula
        else: return -1
    def getNumero(self):
        return self.Numero
    def setNumero(self,Numero):
        self.Numero = Numero
    def getPosicion(self):
        return self.Posicion
    def setPosicion(self,Posicion):
        if Posicion.title() == ("Golero" or "Defensa" or "Mediocampista" or "Delantero"):
            self.Posicion = Posicion.title()
        else: return -1
    def getValoracion(self):
        return self.Valoracion
    def setValoracion(self,Valoracion):
        self.Valoracion = Valoracion
    def Jugar(self,accion:str):
        accion = accion.lower()
        if accion == ("atajar", "marcar", "mover con pelota", "pasar", "pase largo", "interceptar pase", "patear al arco", "despejar"):
            print(f'El jugador numero {self.Numero}, {self.Nombre} realiza {accion}')
        else: return -1
    def Mover(self,Direccion:str,Velocidad:int):
        if Velocidad > 100: Velocidad = 100
        elif Velocidad < 1: Velocidad = 1
        if Velocidad < 60: lentorap = "lenta"
        if Velocidad >= 60: lentorap = "rapida"
        Direccion = Direccion.lower()
        if Direccion == ("arriba" or "abajo"):
            print(f'El jugador numero {self.Numero}, {self.Nombre} se mueve hacia {Direccion} de manera {lentorap}')
        elif Direccion == ("izquierda" or "derecha"):
            print(f'El jugador numero {self.Numero}, {self.Nombre} se mueve hacia la {Direccion} de manera {lentorap}')
        else: return -1
    pass