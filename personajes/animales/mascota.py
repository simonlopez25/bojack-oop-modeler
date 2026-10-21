from personajes.animales.animal import Animal

class Mascota(Animal):
    def __init__(self,nombre,edad,especie,propietario:str):
        super().__init__(nombre,edad,especie)
        self.propietario = propietario

    def presentar(self)->str:
        return f"El nombre de la mascota es: {self.nombre} y su edad es de {self.edad} y su propietario es {self.propietario}"