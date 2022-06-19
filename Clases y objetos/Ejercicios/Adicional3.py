class Hora:
    def __init__(self):
        self.setHora(00)
        self.setMinutos(00)
        self.setSegundos(00)
    def validar(self,hora:int=00,minutos:int=00,segundos:int=00):
        self.setHora(hora)
        self.setMinutos(minutos)
        self.setSegundos(segundos)
    def getHora(self):
        return self.Hora
    def setHora(self,Hora):
        while Hora > 23:
            Hora -= 24
        self.Hora = Hora
    def getMinutos(self):
        return self.Minutos
    def setMinutos(self,Minutos):
        while Minutos > 59:
            Minutos -= 60
        self.Minutos = Minutos
    def getSegundos(self):
        return self.Segundos
    def setSegundos(self,Segundos):
        while Segundos > 59:
            Segundos -= 60
        self.Segundos = Segundos
    def time2segs(self,hrs,mins,segs):
        return segs+(mins*60)+((hrs*60)*60)
    def segs2time(self,segs):
        segs = segs % (24 * 3600)
        hrs = segs // 3600
        segs %= 3600
        mins = segs // 60
        segs %= 60
        return {'segs':segs,'hrs':hrs,'mins':mins}
    def avanzar(self,segundos):
        x = self.time2segs(self.Hora,self.Minutos,self.Segundos)
        x += segundos
        y = self.segs2time(x)
        self.setHora(y['hrs'])
        self.setMinutos(y['mins'])
        self.setSegundos(y['segs'])
    def aSegundos(self):
        return self.time2segs(self.Hora,self.Minutos,self.Segundos)
    def deSegundos(self,segundos):
        self.avanzar(segundos)
    def segundosDesde(self,horas,minutos,segundos):
        x = self.time2segs(horas,minutos,segundos)
        y = self.time2segs(self.Hora,self.Minutos,self.Segundos)
        return abs(x-y)
    def siguiente(self):
        self.avanzar(1)
    def anterior(self):
        self.avanzar(-1)
    def __str__(self):
        return (f'{self.Hora:02d}hs. {self.Minutos:02d}ms. {self.Segundos:02d}s.')
    def copia(self):
        return self

reloj = Hora()
print(reloj)
reloj.avanzar(10)
print(reloj)
reloj.avanzar(100)
print(reloj)
reloj.setHora(25)
print(reloj)
reloj.siguiente()
print(reloj)
reloj.anterior()
print(reloj)
print(reloj.aSegundos())
reloj.setMinutos(1000)
reloj.setSegundos(1000)
reloj.setHora(14)
print(reloj)
print(reloj.segundosDesde(10,20,45))
reloj.validar(10,20)
print(reloj)
reloj.validar(11)
print(reloj)
reloj.validar(10,20,10)
print(reloj)