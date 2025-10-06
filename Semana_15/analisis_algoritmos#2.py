# Analice los siguientes algoritmos usando la Big O Notation:

# print_numbers_times_2

def print_numbers_times_2(numbers_list):# O(n)
    for number in numbers_list:       # O(n)
        print(number * 2)             # O(1)

numbers = [1, 2, 3, 4, 5]            # O(1)
print_numbers_times_2(numbers)        # O(1)

# check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b): # O(n^2)
    for element_a in list_a:           # O(n)
        for element_b in list_b:       # O(n^2)
            if element_a == element_b: # O(1)
                return True            # O(1)
    return False                       # O(1)

list_a = [1, 2, 3] # O(1)
list_b = [3, 4, 5] # O(1)

result = check_if_lists_have_an_equal(list_a, list_b) # O(1)
print(result)                          # O(1)

# print_10_or_less_elements
def print_10_or_less_elements(list_to_print): # O(n)
    list_len = len(list_to_print)       # O(1)
    for index in range(min(list_len, 10)): # O(n)
        print(list_to_print[index])     # O(1)

my_list = [1,2,3,4,5,6,7,8,9,10,11]   # O(1)
print_10_or_less_elements(my_list)     # O(1)

#generate_list_trios
def generate_list_trios(list_a, list_b, list_c): # O(n^3)
    result_list = []                     # O(1)
    for element_a in list_a:             # O(n)
        for element_b in list_b:         # O(n^2)
            for element_c in list_c:     # O(n^3)
                result_list.append(f'{element_a} {element_b} {element_c}') # O(1)

list_a = [1,2]                           # O(1)
list_b = ['a','b']                       # O(1)
list_c = ['x','y']                       # O(1)

result = generate_list_trios(list_a, list_b, list_c) # O(1)
print(result)                             # O(1)
