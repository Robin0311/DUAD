# Ejercicios de Iterables y Listas

# 1-Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Goku', 'Vegeta', 'Gohan', 'Piccolo', 'Frieza', 'Kamehameha']
second_list = ['Super Saiyan', 'Pride', 'Potential', 'Strategy', 'Destruction', 'Wave']

for i in range(len(first_list)):
    print(first_list[i], second_list[i])


# 2-Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

# 1. Pista: investigue de que otras maneras se puede usar el `range`.

name = 'Robinson Cerrato'

for i in range(len(name) - 1, -1, -1):
    print(name[i])

# 3-Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

def names(lst):
    if len(lst) < 2:
        return lst  # Nothing to swap
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = ['Robinson', 'Luis', 'Isabelle', 'Bryan', 'Alex']
result = names(my_list)
print(result)

# 4-Cree un programa que elimine todos los números impares de una lista.

def remove_odds(lst):
    return [num for num in lst if num % 2 == 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = remove_odds(my_list)
print(result)


# 5-Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.print("Enter 10 numbers:")
numbers = []
for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

print("Numbers entered:", numbers)
print("The highest number was", max(numbers))