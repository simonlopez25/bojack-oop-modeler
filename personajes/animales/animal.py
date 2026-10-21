from personajes.personaje import Personaje


class Animal(Personaje):
    def __init__(self, nombre, edad: int, especie: str):
        super().__init__(nombre, edad)
        self.especie = especie

    def presentar(self) -> str:
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy un/a {self.especie}."
