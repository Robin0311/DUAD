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