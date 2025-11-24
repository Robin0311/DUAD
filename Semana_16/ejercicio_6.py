# 6-Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def sort_string_alphabetically(text):
    word_list = text.split('-')           
    word_list.sort()                      
    result = '-'.join(word_list)          
    return result


string = "Robinson-Isabel-Tabata-Alex-Bryan-Maria"
result = sort_string_alphabetically(string)
print(result)