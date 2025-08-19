# 5-Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def count_case(text):
    uppercase = 0
    lowercase = 0
    for letter in text:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
    print("Number of uppercase letters:", uppercase)
    print("Number of lowercase letters:", lowercase)


message = "The Great Adventure of ROBINSON"
count_case(message)