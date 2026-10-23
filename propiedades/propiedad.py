from contratos.habitable import Habitable

class Propiedad(Habitable):
    def __init__(self,ubicacion:str,precio:float):
        self.ubicacion = ubicacion
        self.precio = precio