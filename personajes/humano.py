from personajes.personaje import Personaje

class Humano(Personaje):
    def __init__(self, nombre, edad, profesion:str):
        super().__init__(nombre, edad)
        self.profesion = profesion

    def presentar(self)->str:
        return f"Hola, soy{self.nombre},tengo{self.edad} y trabajo {self.profesion}."

