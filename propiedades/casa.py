from  propiedades.propiedad import Propiedad

class Casa(Propiedad):
    def __init__(self, ubicacion: str, precio: float, tipo: str, habitaciones: int):
        super().__init__(ubicacion, precio)
        self.tipo = tipo
        self.habitaciones = habitaciones

    def descripcion_propiedad(self) -> str:
        return f"una hermosa {self.tipo} ubicada en {self.ubicacion} (Precio: {self.precio}) con {self.habitaciones} habitaciones."