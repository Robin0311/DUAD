# 4-Cree una función que le de la vuelta a un string y lo retorne.

def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text  # Add characters to the front
    return reversed_text


message = "Python is fun"
result = reverse_string(message)
print("Reversed text:", result)