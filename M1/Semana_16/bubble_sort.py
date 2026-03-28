def bubble_sort(list_to_sort):
    
    if not isinstance(list_to_sort, list):
        raise TypeError("list_to_sort must be a list")

    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp

    
    return list_to_sort


if __name__ == "__main__":
    numbers = [54, 12, 56, 32, 48, 76, 14, 2, 99, 25, 40, 8]
    bubble_sort(numbers)
    print(numbers)
