# Implementar una clase modelando una cuenta bancaria. La cuenta bancaria tiene un saldo, un número de cuenta, e
# información sobre el dueño, que es una instancia de la clase anterior (ejercicio 3). La clase debe implementar
# los métodos de hacer un depósito o una extracción de dinero. El método de extracción de dinero debe rechazar la
# transacción si no hay fondos suficientes en la cuenta. También desarrollar una función transferencia que mueve
# un monto entre una y otra cuenta (Para esto se puede realizar una extracción seguido por un depósito). Esos métodos
# y funciones deben devolver un valor lógico indicando si se fue posible ejecutar la transacción.

from Ejercicio3 import persona

class cuenta:
    def __init__(self,Saldo,Numero,Identidad):
        self.Saldo = Saldo
        self.Numero = Numero
        self.Identidad = Identidad
    def deposito(self,deposito):
        self.Saldo += deposito
    def extraccion(self,extraccion):
        if self.Saldo - extraccion >= 0:
            self.Saldo -= extraccion
        else: print('Nao nao')
    def getIdentidad(self):
        return (self.Identidad["nombre"])
    def getSaldo(self):
        return str(self.Saldo)

def transferencia(cuenta1,cuenta2,monto):
    cuenta1.extraccion(monto)
    cuenta2.deposito(monto)
    print(f'Se han transferido {monto}$ de la cuenta {cuenta1.getIdentidad()} a la cuenta {cuenta2.getIdentidad()}')
    print(f'El nuevo monto de la cuenta {cuenta1.getIdentidad()} es de {cuenta1.getSaldo()}')
    print(f'El nuevo monto de la cuenta {cuenta2.getIdentidad()} es de {cuenta2.getSaldo()}')
    
pablo = cuenta(1000,564654,persona.Identificar(persona('3283343','Artigas 292','Pablo','Fuentes','47323492')))
print(pablo.getSaldo())
print('Depositando 100:')
pablo.deposito(100)
print(pablo.getSaldo())
print('Intentado extraer 1500:')
pablo.extraccion(1500)
print(pablo.getSaldo())
print('Extrayendo 1000:')
pablo.extraccion(1000)
print(pablo.getSaldo())

juan = cuenta(10000,5646666,persona.Identificar(persona('6949254','Artigas 295','Juan','Marquez','47323495')))
print('Transferencia de 1000$ de Juan a Pablo')
transferencia(juan,pablo,1000)