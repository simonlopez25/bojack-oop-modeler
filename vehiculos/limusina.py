from vehiculos.vehiculo import Vehiculo

class AutoDeportivo(Vehiculo):
    def __init__(self,marca:str,modelo:str,condiciones:str,lujos:str):
        super().__init__(marca,modelo,condiciones)
        self.lujos = lujos

    def condiciones(self):
        return (f"Este vehiculo es especial de la marca {self.marca} y su modelo {self.modelo} que se fabrico en el año "
                f"{self.ano} se encuentras en un estado {self.condiciones} y en su interior cuenta con {self.lujos}")