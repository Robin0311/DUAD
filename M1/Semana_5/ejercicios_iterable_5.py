# 5-Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.print("Enter 10 numbers:")
numbers = []
for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

print("Numbers entered:", numbers)
print("The highest number was", max(numbers))