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