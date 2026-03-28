# 4.Cree un programa que le pida tres números al usuario y muestre el mayor.
# Ask the user for the numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# Compare to find the largest number
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

# Display the result
print(f"The largest number is: {largest_number}")


# utilice chatgpt para ver que otras opciones podria realizar este mismo
# y  me compartio el utilizar la funcion max()

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))


higher = max(first_number , second_number , third_number )

print(f"The largest number is: {largest_number}")