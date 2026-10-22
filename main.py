from personajes.humano import Humano
from personajes.animales.animal import Animal
from personajes.animales.animal_humanoide import AnimalHumanoide
from personajes.animales.mascota import Mascota
from personajes.animales.animal_salvaje import AnimalSalvaje
from vehiculos.auto_deportivo import AutoDeportivo

if __name__ == '__main__':
    print("_" * 50)
    print("UNIVERSO DE BOJACK HORSEMAN")
    print("_" * 50)

    diane = Humano("Diane Nguyen", 35, "Escritora")
    lucas=Mascota("Lucas", 35, "Perro",diane.nombre)
    porche=AutoDeportivo("Porche", "2016", "Exelentes","20%")


    print(f"{diane.nombre} tiene una mascota llamada {lucas.nombre}, todos los dias va a su trabajo de {diane.profesion}"
          f" y va en su cocoche deportivo de la marca {porche.marca} que salio en el año {porche.modelo}")

