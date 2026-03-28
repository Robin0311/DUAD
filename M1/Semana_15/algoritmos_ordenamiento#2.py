# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort_reverse(list_to_sort):
    n = len(list_to_sort)
    print("First List:", list_to_sort)  
    for i in range(n):
        moved = False
        for j in range(n-1, i, -1):
            print(f"{list_to_sort[j-1]} < {list_to_sort[j]}")
            if list_to_sort[j] < list_to_sort[j-1]:
                print(f"Moving {list_to_sort[j]}")
                list_to_sort[j], list_to_sort[j-1] = list_to_sort[j-1], list_to_sort[j]
                moved = True
                print("current list:", list_to_sort)
        if not moved:
            break
    
    print("List fixed:", list_to_sort)

numbers = [54,12,2,99,25,40,8]
bubble_sort_reverse(numbers)
