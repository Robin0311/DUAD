# Ejercicios de Manejo de Archivos

# 1.Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


def sort_songs(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            songs = [line.strip() for line in file if line.strip()]  # Remove empty lines

        songs.sort()

        with open(output_file, "w", encoding="utf-8") as file:
            for song in songs:
                file.write(song + "\n")

        print(f"Songs sorted and saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


sort_songs("songs.txt", "sorted_songs.txt")

#aqui verifico en la terminal que las canciones antes y despues de ordenarlas
print("\nBefore:\n")
def open_and_print_file(path):
	with open(path) as file:
		print(file.read())
          
open_and_print_file('songs.txt')		


print("\nAfter:\n")


def open_and_print_file(path):
	with open(path) as file:
		print(file.read())
          
open_and_print_file('sorted_songs.txt')		