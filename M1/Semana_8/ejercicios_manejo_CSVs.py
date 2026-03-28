# Ejercicios de Manejo de CSVs

# 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB


import csv

# Ask the user how many games they want to enter
n = int(input("How many video games do you want to enter? "))

# Open the CSV file for writing
with open("video_games.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)  # Comma is default delimiter

    # Write header row
    writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])

    # Collect and write game data
    for i in range(n):
        print(f"\n--- Game {i+1} ---")
        name = input("Enter game name: ")
        genre = input("Enter genre: ")
        developer = input("Enter developer: ")
        esrb = input("Enter ESRB rating: ")
        writer.writerow([name, genre, developer, esrb])

print("\nData saved successfully in 'video_games.csv'")

#imprime en la terminal los datos guardados 
def open_and_print_file(path):
	with open(path) as file:
		print(file.read())
          
open_and_print_file('video_games.csv')	

# 2.Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import csv


n = int(input("How many video games do you want to enter? "))

with open("video_games.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter="\t")  # Tab-separated

    
    writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])

    for i in range(n):
        print(f"\n--- Game {i+1} ---")
        name = input("Enter game name: ")
        genre = input("Enter genre: ")
        developer = input("Enter developer: ")
        esrb = input("Enter ESRB rating: ")
        writer.writerow([name, genre, developer, esrb])

print("\n✅ Data saved successfully in 'video_games.csv'")


#imprime en la terminal los datos guardados 
def open_and_print_file(path):
	with open(path) as file:
		print(file.read())
          
open_and_print_file('video_games.csv')	

