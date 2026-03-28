# Crea un bubble_sort por tu cuenta sin revisar el código de la lección

def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort)-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j+1]
                list_to_sort[j+1] = temp

numbers = [54,12,56,32,48,76,14,2,99,25,40,8]
bubble_sort(numbers)
print(numbers)