# Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort(list_to_sort): # O(n^2)
    for outer_index in range(0, len(list_to_sort) - 1): # O(n)
        has_made_changes = False  
        for index in range(0, len(list_to_sort) - 1 - outer_index):# O(n^2)
            current_element = list_to_sort[index] # O(1)
            next_element = list_to_sort[index + 1] # O(1)
            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}') # O(1)
            if current_element > next_element: # O(1)
                print('El elemento actual es mayor al siguiente. Intercambiandolos...') # O(1)
                list_to_sort[index] = next_element # O(1)
                list_to_sort[index + 1] = current_element # O(1)
                has_made_changes = True # O(1)
    if not has_made_changes: # O(1)
        return # O(1)


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8] # O(1)
bubble_sort(my_test_list) # O(1)

print(my_test_list)# O(1)