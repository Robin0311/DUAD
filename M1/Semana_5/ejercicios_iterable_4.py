# 4-Cree un programa que elimine todos los números impares de una lista.

def remove_odds(lst):
    return [num for num in lst if num % 2 == 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = remove_odds(my_list)
print(result)