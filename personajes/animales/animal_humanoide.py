from personajes.animales.animal import Animal

class AnimalHumanoide(Animal):
    def __init__(self, nombre:str,edad:int,especie:str,ocupacion:str):
        super().__init__(nombre,edad,especie)
        self.ocupacion = ocupacion

    def presentar(self)->str:
        return f"hola mi nombre es {self.nombre} tengo la edad de {self.edad} años, mi especie es {self.especie} y mi ocupacion es {self.ocupacion}"