# Ejercicios de Funciones

# 1- Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def name():
    print ("My name is Robinson")
    last_name()


def last_name():
    print("My lastname is Cerrato")

name()

# 2-Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor.

def clothe():
    types_clothes = "Theres a lot of types of clothes"
    print (types_clothes)
    

print(types_clothes)

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


# 3-Cree una función que retorne la suma de todos los números de una lista.


def sum_elements(numbers):
    return sum(numbers)


my_list = [4, 6, 2, 29]
result = sum_elements(my_list)
print("The sum is:", result)


# 4-Cree una función que le de la vuelta a un string y lo retorne.

def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text  # Add characters to the front
    return reversed_text


message = "Python is fun"
result = reverse_string(message)
print("Reversed text:", result)


# 5-Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def count_case(text):
    uppercase = 0
    lowercase = 0
    for letter in text:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
    print("Number of uppercase letters:", uppercase)
    print("Number of lowercase letters:", lowercase)


message = "The Great Adventure of ROBINSON"
count_case(message)


# 6-Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def sort_string_alphabetically(text):
    word_list = text.split('-')           
    word_list.sort()                      
    result = '-'.join(word_list)          
    return result


string = "Robinson-Isabel-Tabata-Alex-Bryan-Maria"
result = sort_string_alphabetically(string)
print(result)


# 7-Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


numbers = [1, 4, 6, 7, 13, 9, 67, 27, 99, 54, 41]
result = filter_primes(numbers)
print(result)

