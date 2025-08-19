# Ejercicios de Diccionarios

# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#     - `nombre`
#     - `numero_de_estrellas`
#     - `habitaciones`
# - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#     - `numero`
#     - `piso`
#     - `precio_por_noche`
hotel = {
    "name": "Paradise Hotel",
    "star_rating": 5,
    "rooms": [
        {
            "number": 101,
            "floor": 1,
            "price_per_night": 120
        },
        {
            "number": 202,
            "floor": 2,
            "price_per_night": 150
        },
        {
            "number": 303,
            "floor": 3,
            "price_per_night": 180
        }
    ]
}
print(hotel)

# 2-Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
country = ['Costa Rica', 'Argentina', 'Spain']
capital = ['San Jose', 'Buenos Aires', 'Madrid']


place = dict(zip(country, capital))
print(place)

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