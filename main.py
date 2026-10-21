from personajes.humano import Humano
from personajes.animal import Animal

if __name__ == '__main__':
    print(f"_"*50)
    print(f"Animals")
    diane = Humano("Diane Nguyen", 35, "Escritora")
    print(f"{diane.nombre} - {diane.edad} - {diane.profesion}")

    print(f"_" * 50)
    print(f"Animales")

    lucas = Animal("Lucas", 35, "Perro")
    print(f"{lucas.nombre} - {lucas.edad} - {lucas.especie}")
