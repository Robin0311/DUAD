# Ejercicios de Manejo de JSON (adjunto el archivo json “pokemons.json”)

# 1. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def load_pokemons(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_pokemons(file_path, pokemons):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=2, ensure_ascii=False)


def add_pokemon(pokemons):
    print("\n--- Add a New Pokémon ---")
    name = input("Name (English): ")
    types = input("Type(s) (separated by commas): ").split(",")
    types = [t.strip() for t in types]

    print("\nEnter base stats:")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    new_pokemon = {
        "name": {"english": name},
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    pokemons.append(new_pokemon)
    return pokemons


def main():
    file_path = "pokemons.json"
    pokemons = load_pokemons(file_path)
    pokemons = add_pokemon(pokemons)
    save_pokemons(file_path, pokemons)
    print(f"\n Pokémon added and saved to '{file_path}'.")

if __name__ == "__main__":
    main()

#abre el archivo en la terminal 
def open_and_print_file(path):
	with open(path) as file:
		print(file.read())
          
open_and_print_file('pokemons.json')	