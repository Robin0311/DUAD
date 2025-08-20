# 2-Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
country = ['Costa Rica', 'Argentina', 'Spain']
capital = ['San Jose', 'Buenos Aires', 'Madrid']


place = dict(zip(country, capital))
print(place)