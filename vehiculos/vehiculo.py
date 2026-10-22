from contratos.conducible import Conducible

class Vehiculo(Conducible):
    def __init__(self,marca:str,modelo:str,condiciones:str):
        self.marca = marca
        self.modelo = modelo
        self.condiciones = condiciones