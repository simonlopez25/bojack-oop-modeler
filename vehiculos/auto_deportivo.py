from vehiculos.vehiculo import Vehiculo

class AutoDeportivo(Vehiculo):
    def __init__(self,marca:str,modelo:str,condiciones:str,rareza:str):
        super().__init__(marca,modelo,condiciones)
        self.rareza = rareza

    def conducir(self):
        return (f"Estoy conduciendo uno de los autos deportivos exclusivos de la marca {self.marca}, modelo {self.modelo}"
                f"del año {self.ano}, condiciones {self.condiciones} y la rareza de este tipo de vehivulos es de un 40% debido"
                f"a las cantidad de unidades que salieron al mercado {self.rareza}")
