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