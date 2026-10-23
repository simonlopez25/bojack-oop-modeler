from personajes.humano import Humano
from personajes.animales.animal import Animal
from personajes.animales.animal_humanoide import AnimalHumanoide
from personajes.animales.mascota import Mascota
from personajes.animales.animal_salvaje import AnimalSalvaje
from vehiculos.auto_deportivo import AutoDeportivo
from propiedades.casa import Casa

if __name__ == '__main__':
    print("_" * 50)
    print("UNIVERSO DE BOJACK HORSEMAN")
    print("_" * 50)

    diane = Humano("Diane Nguyen", 35, "Escritora")
    lucas = Mascota("Lucas", 35, "Perro", diane.nombre)
    porche = AutoDeportivo("Porche", "2016", "Excelentes", "20%")

    home = Casa("Florida", "200000", "Duplex", 4)

    print(
        f"{diane.nombre} vive en una casa en la ciudad de {home.ubicacion}, tiene una mascota llamada {lucas.nombre}, todos los días va a su trabajo de {diane.profesion}"
        f" y va en su coche deportivo de la marca {porche.marca} que salió en el año {porche.modelo}.")
    print("_" * 50)