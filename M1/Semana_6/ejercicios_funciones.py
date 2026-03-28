# Ejercicios de Funciones

# 1- Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def name():
    print ("My name is Robinson")
    last_name()


def last_name():
    print("My lastname is Cerrato")

name()



# a- no se puede accesar a la variable types_clothes porque fue creada dentro de la function y solo existe si la function se ejecuta
counter = 0  # Global variable


def increase():
    global counter  # Tell Python we want to use the global variable
    counter += 1
    print("Counter inside the function:", counter)

increase()
increase()

print("Counter outside the function:", counter)
# No se puede cambiar el valor de una variable global fuera de una funcion si queremos cambiarlo debemos utlizar global antes de la variable global que tratamos de modificar