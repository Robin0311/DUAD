# 3-Cree un programa que use una lista para eliminar keys de un diccionario.
employee = {
    'name': 'Robinson',
    'email': 'Robinson@gmail.com',
    'level': 1,
    'age': 32
}

list_of_keys = ['level', 'age']
for key in list_of_keys:
    employee.pop(key) 
print(employee)