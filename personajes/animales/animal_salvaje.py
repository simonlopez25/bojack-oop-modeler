from personajes.animales.animal import Animal

class AnimalSalvaje(Animal):
    def __init__(self,nombre,edad,especie,habitat:str):
        super().__init__(nombre,edad,especie)
        self.habitat = habitat

    def presentar(self)->str:
        return f"el nombre del animal salvaje {self.nombre} y pertene a la especie {self.especie}, tiene una edad aproximada de {self.edad} años  y vive por lo general en el habiat {self.habitat}"
