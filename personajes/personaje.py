from contratos.presentable import Presentable

class Personaje(Presentable):
    def __init__(self, nombre:str,edad:int):
        self.nombre = nombre
        self.edad = edad