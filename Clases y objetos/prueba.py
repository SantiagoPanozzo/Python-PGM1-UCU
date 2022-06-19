from tkinter import W


class auto:
    # soy un auto
    def __init__(self,color,material=''): #si no pasamos nada material va a estar vacio
        self.color = color
        self.material = material
    def avanzar(self):
        print('room')
    def getColor(self):
        return self.color

elauto = auto('rojo','metal')
print(elauto)
print(elauto.color)
print(elauto.material)
elauto.avanzar()