##Ejercicios de Sintaxis

##1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
# 1. string + string
print("Hello " + "World")  # Output: "Hello World"

# 2. string + int
# print("age: " + 25)       # cannot add str + int

# 3. int + string
print(10 + " years")        # cannot add int + str

# 4. list + list
print([1, 2] + [3, 4])      # Output: [1, 2, 3, 4]

# 5. string + list
print("List: " + [1, 2])    # str + list is not valid

# 6. float + int
print(3.5 + 2)              # Output: 5.5

# 7. bool + bool
print(True + True)          # Output: 2

# `str + str` concatena.
# `list + list` concatena listas.
# `int + float` hace suma normal.
# `str + int` o `str + list` causan error: debe **convertir** primero con `str()`. ''

# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre
# si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
# Solicitar datos al usuario
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Clasificación por edad
if age < 3:
    category = "baby"
elif age < 12:
    category = "child"
elif age < 15:
    category = "preteen"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
elif age < 60:
    category = "adult"
else:
    category = "senior adult"

# mostrar resultado
print(f"{first_name} {last_name}, you are {age} years old and you are a {category}.")


# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

para generar numeros aletorios  se utiliza el modulo random hay
 otros modulos utiles para cada situacion siempre se inician usando la palabra import

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Variable to store the user's guess
guess = 0
print("Guess the secret number between 1 and 10!")

# Loop until the user guesses correctly
while guess != secret_number:
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print("Correct! You guessed the number.")

# 4.Cree un programa que le pida tres números al usuario y muestre el mayor.
# Ask the user for the numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# Compare to find the largest number
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

# Display the result
print(f"The largest number is: {largest_number}")


# utilice chatgpt para ver que otras opciones podria realizar este mismo
# y  me compartio el utilizar la funcion max()

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))


higher = max(first_number , second_number , third_number )

print(f"The largest number is: {largest_number}")

# 5.Dada n cantidad de notas de un estudiante, calcular:
# 1. Cuantas notas tiene aprobadas (mayor a 70).
# 2. Cuantas notas tiene desaprobadas (menor a 70).
# 3. El promedio de todas.
# 4. El promedio de las aprobadas.
# 5. El promedio de las desaprobadas.

# Variables
total_grades = 0
grade_counter = 1
current_grade = 0
passed_grades_count = 0
failed_grades_count = 0
average_passed_grades = 0
average_failed_grades = 0
overall_average = 0

print("Enter the total number of grades:")

total_grades = int(input())

while grade_counter <= total_grades:
    print("Enter grade number")
    print(grade_counter)
    
    current_grade = float(input())

    if current_grade < 70:
        failed_grades_count += 1
        average_failed_grades += current_grade
    else:
        passed_grades_count += 1
        average_passed_grades += current_grade

    overall_average += (current_grade / total_grades)

    grade_counter += 1

# Calculate average of failed grades (if any)
if failed_grades_count > 0:
    average_failed_grades = average_failed_grades / failed_grades_count
else:
    average_failed_grades = 0

# Calculate average of passed grades (if any)
if passed_grades_count > 0:
    average_passed_grades = average_passed_grades / passed_grades_count
else:
    average_passed_grades = 0

# Display results
print("The student has this number of passing grades:")
print(passed_grades_count)

print("This is the average of the passing grades:")
print(f"{average_passed_grades:.2f}")

print("The student has this number of failing grades:")
print(failed_grades_count)

print("This is the average of the failing grades:")
print(f"{average_failed_grades:.2f}")

print("This is the overall average grade:")
print(f"{overall_average:.2f}")

