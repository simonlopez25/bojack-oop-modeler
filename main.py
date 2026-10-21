from personajes.humano import Humano
from personajes.animales.animal import Animal
from personajes.animales.animal_humanoide import AnimalHumanoide
from personajes.animales.mascota import Mascota
from personajes.animales.animal_salvaje import AnimalSalvaje

if __name__ == '__main__':
    print("_" * 50)
    print("UNIVERSO DE BOJACK HORSEMAN")
    print("_" * 50)

    diane = Humano("Diane Nguyen", 35, "Escritora")
    print(diane.presentar())

    print("-" * 50)

    lucas = Animal("Lucas", 5, "Perro")
    print(lucas.presentar())

    print("-" * 50)

    bojack = AnimalHumanoide("Bojack", 5, "Caballo","Actor")
    print(bojack.presentar())

    print("-" * 50)

    Lupe= Mascota("Lupe", 5, "Perro",bojack.nombre)
    print(Lupe.presentar())

    print("-" * 50)

    Jaguar=AnimalSalvaje("Tito", 5, "jaguar o felinos","Jungla")
    print(Jaguar.presentar())